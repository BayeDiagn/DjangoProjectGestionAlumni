from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from Cursus.models import Cursus
from Emploi.models import Emploi
from Etudiants.forms import EtudiantForm, EtudiantFormUpdate
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from Etudiants.models import Etudiant
from competence.models import Competence
#from django.contrib.auth.views import LogoutView








@login_required
def etudiant_home(request):
    user = request.user
    cursus = Cursus.objects.filter(etudiant=user.id)
    emploi = Emploi.objects.filter(etudiant=user.id)
    competences = Competence.objects.filter(etudiant=user.id)
    #nbre=Cursus.objects.count();
        
    context={"cursus":cursus,"emploi":emploi,"competences":competences}
    return render(request, "Etudiants/etudiant_home.html",context)


#view d'inscription
def etudiant_inscription(request):
    form = EtudiantForm()
    if request.method == 'POST':
        form = EtudiantForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("cursus",user.id)
    context={"form":form}
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
    if request.method == 'POST':
        form = EtudiantFormUpdate(request.POST,request.FILES,instance=etudiant)
        if form.is_valid():
             form.save()
        return redirect("/")
    context={"form":form,"etudiant":etudiant}
    return render(request, "Etudiants/modifier.html",context)
