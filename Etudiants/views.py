from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from Cursus.models import Cursus
from Emploi.models import Emploi
from Etudiants.forms import EtudiantForm, EtudiantFormUpdate, PhotoCouvertureForm, PhotoProfilForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from Etudiants.models import Etudiant, PhotoCouverture, PhotoProfil
from competence.models import Competence
#from django.contrib.auth.views import LogoutView
from django.db.models import Case, When
from django.db.models import OuterRef, Subquery
from django.db.models import Q,F
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
import hashlib



















@login_required
def etudiant_home(request):
    user = request.user
    cursus = Cursus.objects.filter(etudiant=user.id)
    emploi = Emploi.objects.filter(etudiant=user.id)
    competences = Competence.objects.filter(etudiant=user.id)
    user_profession_upper = request.user.profession.upper()
    
    photo_profil = PhotoProfil.objects.filter(etudiant=user.id).last()
    photo_couvertures1 = PhotoCouverture.objects.filter(etudiant=user.id).last()
    photo_couvertures2= PhotoCouverture.objects.filter(etudiant=user.id).order_by('-id')


    chemin_photo_profil = photo_profil.profil.url
    
    
    chemin_photo_couverture1 = photo_couvertures1.couverture.url if photo_couvertures1 else None
    
    photo_couverture2 = photo_couvertures2[1] if len(photo_couvertures2) > 1 else None
    chemin_photo_couverture2 = photo_couverture2.couverture.url if photo_couverture2 else None
    #nbre=Cursus.objects.count();
    
   
    context={"cursus":cursus,"emploi":emploi,"competences":competences,"user_profession_upper":user_profession_upper,"chemin_photo_profil":chemin_photo_profil,"chemin_photo_couverture1":chemin_photo_couverture1,"chemin_photo_couverture2":chemin_photo_couverture2}
    return render(request, "Etudiants/etudiant_home.html",context)


#view d'inscription
def etudiant_inscription(request):
    form = EtudiantForm()
    photo_profil_form = PhotoProfilForm()
    photo_couverture_form = PhotoCouvertureForm()

    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        photo_profil_form = PhotoProfilForm(request.POST, request.FILES)
        photo_couverture_form = PhotoCouvertureForm(request.POST, request.FILES)
        
        if form.is_valid() and photo_profil_form.is_valid() and photo_couverture_form.is_valid():
            user = form.save()
            
            photo_profil = photo_profil_form.save(commit=False)
            photo_profil.etudiant = user
            photo_profil.save()

            photo_couverture = photo_couverture_form.save(commit=False)
            photo_couverture.etudiant = user
            photo_couverture.save()
            
            return redirect("cursus",user.id)
        
    context={"form":form,"photo_profil_form": photo_profil_form,"photo_couverture_form": photo_couverture_form,}
    return render(request, "Etudiants/inscription.html",context)


#view de connexion
def etudiant_login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect("etudiant_home")
            
            #message = f'Bonjour, {user.prenom} Vous êtes connecté.'
        else:
            messages.error(request, 'Identifiants invalides')
            
    return render(request, "Etudiants/login.html")


#view de deconnexion
def etudiant_logout(request):
    logout(request)
    return redirect("login")

#view update
def etudiant_update(request,pk):
    #user=request.user
    etudiant=Etudiant.objects.get(id=pk)
    
    form = EtudiantFormUpdate(instance=etudiant)
    photo_profil_form = PhotoProfilForm()
    photo_couverture_form = PhotoCouvertureForm()
    
    if request.method == 'POST':
        form =  EtudiantFormUpdate(request.POST,instance=etudiant)
        photo_profil_form = PhotoProfilForm(request.POST, request.FILES)
        photo_couverture_form = PhotoCouvertureForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            form.save()
            
        if photo_profil_form.is_valid() and photo_profil_form.cleaned_data['profil']:  #form vide est cosiderer comme valide 
                                                                                               #donc on verifie si le champ contient une photo
            photo_profil = photo_profil_form.save(commit=False)
            photo_profil.etudiant = request.user
            photo_profil.save()
            
        if photo_couverture_form.is_valid() and photo_couverture_form.cleaned_data['couverture']:
            photo_couverture = photo_couverture_form.save(commit=False)
            photo_couverture.etudiant = etudiant
            photo_couverture.save()
            #return redirect("/")
            
        
    context={"form":form,"photo_profil_form": photo_profil_form,"photo_couverture_form": photo_couverture_form,"etudiant":etudiant}
    return render(request, "Etudiants/modifier.html",context)



def liste_etudiant(request,pk):
    user = request.user
    #user_id=user.id
    user=user.code_permenant[:2]
    etudiants = Etudiant.objects.exclude(id__in=[1]).order_by(   
        Case(
            When(code_permenant__startswith=user, then=0),
            default=1,
        ),
        'code_permenant'
    )
    photos=PhotoProfil.objects.all()
    cursus = Cursus.objects.all() 
    
   
    
    p=Paginator( etudiants,6)
    page=request.GET.get('page')
    liste=p.get_page(page)  
    
      

    #Etudiant.objects.exclude(Q(id=1) | Q(nom="Doe")) exlure ou filter plusieurs chose on import Q
    #for etudiant in etudiants:  
        #try:
        #photo = PhotoProfil.objects.filter(etudiant=etudiant).last()  #latest il faut leve l'exception
        #chemin = photo.profil.url if photo else None
        #nom_complet = photo.profil.name
        #print(chemin)
        #except PhotoProfil.DoesNotExist:   
         #   print("Pas de photo")
        
    context={'etudiants': etudiants,"photos":photos,"cursus":cursus,"liste":liste}
    return render(request,"Etudiants/liste_etudiant.html",context)



def etudiant_page(request,pk):
    etudiant=Etudiant.objects.get(id=pk)
    
    cursus = Cursus.objects.filter(etudiant=etudiant.id)
    emploi = Emploi.objects.filter(etudiant=etudiant.id)
    competences = Competence.objects.filter(etudiant=etudiant.id)
    
    photo_profil = PhotoProfil.objects.filter(etudiant=etudiant.id).last()
    photo_couvertures1 = PhotoCouverture.objects.filter(etudiant=etudiant.id).last()
    photo_couvertures2= PhotoCouverture.objects.filter(etudiant=etudiant.id).order_by('-id')


    chemin_photo_profil = photo_profil.profil.url
     
    chemin_photo_couverture1 = photo_couvertures1.couverture.url if photo_couvertures1 else None 
    
    photo_couverture2 = photo_couvertures2[1] if len(photo_couvertures2) > 1 else None
    chemin_photo_couverture2 = photo_couverture2.couverture.url if photo_couverture2 else None
    
    context={"etudiant":etudiant,"cursus":cursus,"emploi":emploi,"competences":competences,"chemin_photo_profil":chemin_photo_profil,"chemin_photo_couverture1":chemin_photo_couverture1,"chemin_photo_couverture2":chemin_photo_couverture2}
    
    return render(request,'Etudiants/etudiant.html',context)