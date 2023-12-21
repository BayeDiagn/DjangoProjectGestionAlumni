import datetime
from django.shortcuts import render,redirect
from Cursus.models import Cursus
from Emploi.models import Emploi
from Etudiants.models import Etudiant, PhotoProfil
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q,F
import random
from django.db.models.functions import Lower
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from django.contrib.auth.hashers import make_password

from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from Personnels.models import Personnel

















#decorateur
def personnel_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and user.is_personnel,
        login_url='personnel_login'
    )(view_func)
    return decorated_view_func


@personnel_required
def personnel_home(request):
    etudiants=Etudiant.objects.all().order_by('code_permenant')
    photos = PhotoProfil.objects.all()
    nbre_etudiant=etudiants.count()
    nbre_personnel=Personnel.objects.count()
    
    p=Paginator( etudiants,10)
    page=request.GET.get('page')
    liste=p.get_page(page)
    
    date = datetime.datetime.now()
    jour=date.strftime('%d')
    mois=date.strftime('%m')
    annee=date.strftime('%Y')
    heure=date.strftime('%H')
    mn=date.strftime('%M')
    #print(jour)
    
    #liste_cycle_name=[]
    liste_cycle_nbre=[]
    list_pourcentage=[]
    cycles_nbre = Cursus.objects.count()
    cycles = Cursus.objects.values('cycle').annotate(nbre=Count('id'))
    for cycle_name in cycles:
        #liste_cycle_name.append(cycle_name['cycle'])
        liste_cycle_nbre.append(cycle_name['nbre'])
    #liste_cycle_nbre=list(reversed(liste_cycle_nbre))
    for valeur in liste_cycle_nbre:
        list_pourcentage.append(valeur*100/cycles_nbre)
    data_tuples1 = zip(cycles,list_pourcentage)
    data_tuples2 = zip(cycles,list_pourcentage)
    #etudiants_master = Cursus.objects.filter(cycle='Master').count()
    
    etudiants_lic = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='licence').count()
    etudiants_master = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='master').count()
    #etudiants_master = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='master').count()
    etudiants_lic_mast = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),Q(cycle__icontains='master') | Q(cycle__icontains='licence')).count()
    
    etudiants_lic1 = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='licence').count()
    etudiants_master1 = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='master').count()
    etudiants_lic_mast1 = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),Q(cycle__icontains='master') | Q(cycle__icontains='licence')).count()
    #print(cyc,cyc2,cyc1)
    
    #print(Cursus.objects.filter(etablissement__icontains="alioune diop",cycle="Master").exclude(Q(cycle="Licence") & Q(etablissement__icontains="alioune diop")))
    
    master_alioune = Etudiant.objects.filter(cursus__etablissement__icontains="alioune diop",cursus__cycle="Master")
    nbre_master_alioune = Etudiant.objects.filter(cursus__etablissement__icontains="alioune diop",cursus__cycle="Master").count()
    licence_alioune = Etudiant.objects.filter(cursus__etablissement__icontains="alioune diop",cursus__cycle="Licence")
    etudiants_master_seul = len(set(master_alioune) - set(licence_alioune))
    licence_master = nbre_master_alioune - etudiants_master_seul
    
    master_ailleur=Cursus.objects.filter(cycle__icontains='master').exclude(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb')).count()
    #print(set(licence_alioune)-set(master_alioune))
    #print(master_ailleur)
    
    #print(Etudiant.objects.filter(id__in=etudiants_master_ids))
    #print(Cursus.objects.filter(cycle__etudiant='Master'))


    #etudiants_master_sans_licence = master_alioune.filter(etudiant__in=master_alioune)etudiant__in=licence_alioune).values_list('etudiant_id', flat=True)
    #print(etudiants_master_sans_licence)
    
    #print(liste_cycle_name,cycles_nbre)
    #print(list_pourcentage)
       
    context={'etudiants': etudiants,"photos":photos,"liste":liste,
             "jour":jour,"mois":mois,"annee":annee,"heure":heure,
             "mn":mn,"nbre_etudiant":nbre_etudiant,"cycles":cycles,
             "data_tuples1":data_tuples1,"data_tuples2":data_tuples2,
             "cycles_nbre":cycles_nbre,"etudiants_lic":etudiants_lic,
             "etudiants_master":etudiants_master,"etudiants_lic_mast":etudiants_lic_mast,
             "etudiants_lic1":etudiants_lic1,"etudiants_master1":etudiants_master1,"etudiants_lic_mast1":etudiants_lic_mast1,
             "nbre_personnel":nbre_personnel,"etudiants_master_seul":etudiants_master_seul,
             "licence_master":licence_master,"master_ailleur":master_ailleur,
             } 
    return render(request, "Personnels/personnel.html",context)




def personnel_graphic(request):
    
    liste_entrep_name=[]
    liste_entrep_nbre=[]
    #entreprises = Emploi.objects.values('entreprise').annotate(nbre=Count('id'))   #entreprises = Emploi.objects.values_list('entreprise', flat=True).distinct()
    entreprises = (Emploi.objects.annotate(lower_entreprise=Lower('entreprise')).values('lower_entreprise').annotate(nbre=Count('id')))
    for emploi in entreprises:
        liste_entrep_nbre.append(emploi['nbre'])
        liste_entrep_name.append(emploi['lower_entreprise'])
        #print(f"{emploi['entreprise']} : {emploi['nbre']} emplois")
    #print(liste_entrep_name)
    
    liste_cont_name=[]
    liste_cont_nbre=[]
    typecontrat = (Emploi.objects.annotate(lower_typecont=Lower('typecont')).values('lower_typecont').annotate(nbre=Count('id')))
    for contrat in typecontrat:
        liste_cont_nbre.append(contrat['nbre'])
        liste_cont_name.append(contrat['lower_typecont'])
    #print(typecontrat)
    
    contbyEntrep = {}

    for entrep_name in liste_entrep_name:
        result = (Emploi.objects
        .annotate(lower_entreprise=Lower('entreprise')) 
        .filter(lower_entreprise=entrep_name).annotate(lower_typecont=Lower('typecont')) 
        .values('lower_typecont')
        .annotate(nbre=Count('id'))
    )
        contbyEntrep[entrep_name] = result 
    #print(contbyEntrep)
    
    nbre_TypeCont_By_Entrep =[]
    name_Entrep_TypeCont_By =[]
    for entrep_name, result in contbyEntrep.items():
        for nbre in result:
            nbre_TypeCont_By_Entrep.append(nbre['nbre'])
            name_Entrep_TypeCont_By.append(entrep_name+"_"+nbre['lower_typecont'])

    name_Entrep_TypeCont_By=[upper.upper() for upper in name_Entrep_TypeCont_By]
         
    #print(nbre_TypeCont_By_Entrep)
    #print(name_Entrep_TypeCont_By)
    
    colors = [
        "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])  
        for i in range(len(liste_entrep_name))
    ]
    #emplois_par_entreprise = Emploi.objects.values('entreprise').annotate(nbre=Count('id')).order_by('-nbre')
    #for emploi in emplois_par_entreprise:
       # print(f"{emploi['entreprise']} : {emploi['nbre']} emplois")  #Django sait alors qu'on veut grouper par entrepriseannotate(nbre=Count('id')) compte le nombre d'enregistrements (id) dans chaque groupe d'entreprise
    
    context={"liste_entrep_nbre":liste_entrep_nbre,"liste_entrep_name":liste_entrep_name,
             "colors":colors,"liste_cont_nbre":liste_cont_nbre,"liste_cont_name":liste_cont_name,
             "nbre_TypeCont_By_Entrep":nbre_TypeCont_By_Entrep,"name_Entrep_TypeCont_By":
             name_Entrep_TypeCont_By,
             }
    mot_de_passe_en_clair = "123"
    mot_de_passe_crypte = make_password(mot_de_passe_en_clair)
    print(mot_de_passe_crypte)
    
    return render(request,"Personnels/graphics.html",context)


#def personnel_login(request):
  #  if request.method == 'POST':
   #     form = PersonnelLoginForm(request.POST)
    #    if form.is_valid():
     #       email = form.cleaned_data['email']
      #      password = form.cleaned_data['password']
       #     user = authenticate(request, email=email, password=password)
        #    if user is not None:
         #       login(request, user)
          #      return redirect('personnel_home')
   # else:
   #     form = PersonnelLoginForm()

    #return render(request, 'Personnels/personnel_login.html', {'form': form})
    

class PersonnelLoginView(LoginView):
    template_name = "Personnels/personnel_login.html"
    
    def get_success_url(self):
           return reverse_lazy('personnel_home')



#view de deconnexion
def personnel_logout(request):
    logout(request)
    
    return redirect("personnel_login")