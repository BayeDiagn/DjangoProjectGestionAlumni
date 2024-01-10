import datetime
import json
from django.contrib import messages
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
from django.views.generic import DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from Personnels.models import Personnel
from competence.models import Competence

















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
    #etudiants_json = json.dumps(etudiants)
    photos = PhotoProfil.objects.all()
    nbre_etudiant=etudiants.count()
    nbre_personnel=Personnel.objects.count()
    
    if request.method == "GET":
        searched = request.GET.get('search')
        if searched is not None:
            etudiants= Etudiant.objects.filter(code_permenant__contains=searched).order_by('code_permenant')
    
    p=Paginator( etudiants,10)
    page=request.GET.get('page')
    liste=p.get_page(page)
    
    
    date = datetime.datetime.now()
    jour=date.strftime('%d')
    mois=date.strftime('%m')
    annee=date.strftime('%Y')
    heure=date.strftime('%H')
    mn=date.strftime('%M')
    #print(datetime.date.today())
    
    #liste_cycle_name=[]
    liste_cycle_nbre=[]
    list_pourcentage=[]
    cycles_nbre = Cursus.objects.count()
    cycles = Cursus.objects.values('cycle').annotate(nbre=Count('id'))   #.values('cycle'): permet d'effectuer une opération de regroupement sur un champ
                                                                         #.annotate(): permet de compter pour chaque groupe le nbre d'elts en utilisant leur id
                                                                         #cycles = Cursus.objects.only('cycle') colonne cycle seule
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
    #etudiants_master = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),cycle__icontains='master').count()
   # etudiants_lic_mast = Cursus.objects.filter(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb'),Q(cycle__icontains='master') | Q(cycle__icontains='licence')).count()
     
    #print(etudiants_master)
    
    #print(Cursus.objects.filter(etablissement__icontains="alioune diop",cycle="Master").exclude(Q(cycle="Licence") & Q(etablissement__icontains="alioune diop")))
    
    master_alioune = Etudiant.objects.filter(Q(cursus__etablissement__icontains='alioune diop') | Q(cursus__etablissement__icontains='uadb'),cursus__cycle="Master")
    nbre_master_alioune = master_alioune.count()
    #print(nbre_master_alioune)
    licence_alioune = Etudiant.objects.filter(Q(cursus__etablissement__icontains="alioune diop") | Q(cursus__etablissement__icontains='uadb') ,cursus__cycle="Licence")
    etudiants_master_seul = len(set(master_alioune) - set(licence_alioune))
    licence_master = nbre_master_alioune - etudiants_master_seul
    
    master_ailleur=Cursus.objects.filter(cycle__icontains='master').exclude(Q(etablissement__icontains='alioune diop') | Q(etablissement__icontains='uadb')).count()
    #print(set(licence_alioune)-set(master_alioune))
    #print(master_ailleur)
    
    #print(Etudiant.objects.filter(id__in=etudiants_master_ids))
    
    #list_messages = messages.get_messages(request)
    
       
    context={'etudiants': etudiants,"photos":photos,"liste":liste,
             "jour":jour,"mois":mois,"annee":annee,"heure":heure,
             "mn":mn,"nbre_etudiant":nbre_etudiant,"cycles":cycles,
             "data_tuples1":data_tuples1,"data_tuples2":data_tuples2,
             "cycles_nbre":cycles_nbre,"etudiants_lic":etudiants_lic,
             "nbre_personnel":nbre_personnel,"etudiants_master_seul":etudiants_master_seul,
             "licence_master":licence_master,"master_ailleur":master_ailleur,
             } 
    return render(request, "Personnels/personnel.html",context)




def personnel_graphic(request):
    
    liste_entrep_name=[]
    liste_entrep_nbre=[]
    #entreprises = Emploi.objects.values('entreprise').annotate(nbre=Count('id'))   #entreprises = Emploi.objects.values_list('entreprise', flat=True).distinct()
    entreprises = (Emploi.objects.annotate(lower_entreprise=Lower('entreprise')).values('lower_entreprise').annotate(nbre=Count('id')))   #Emploi.objects.annotate(lower_entreprise=Lower('entreprise')) 
                                                                                                                                          #pour chaque objet Emploi de la base de données, va ajouter 
                                                                                                                                          #un nouveau champ lower_entreprise contenant le champ entreprise 
                                                                                                                                          #original mais converti en minuscules
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
    #print()
    
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
    
    nbre_type_contrat = Emploi.objects.values('typecont').count()
    colors_nbre_typecont = [
        "#"+''.join([random.choice('8ABC1DE6F0234579') for j in range(6)])  
        for i in range(nbre_type_contrat)
    ]

    context={"liste_entrep_nbre":liste_entrep_nbre,"liste_entrep_name":liste_entrep_name,
             "colors":colors,"liste_cont_nbre":liste_cont_nbre,"liste_cont_name":liste_cont_name,
             "nbre_TypeCont_By_Entrep":nbre_TypeCont_By_Entrep,"name_Entrep_TypeCont_By":
             name_Entrep_TypeCont_By,"colors_nbre_typecont":colors_nbre_typecont
             }
    #mot_de_passe_en_clair = "123"
    #mot_de_passe_crypte = make_password(mot_de_passe_en_clair)
    #print(mot_de_passe_crypte)
    
    return render(request,"Personnels/graphics.html",context)



     #email = form.cleaned_data['email']
     #password = form.cleaned_data['password']
    

class PersonnelLoginView(LoginView):
    template_name = "Personnels/personnel_login.html"
    
    def get_success_url(self):
           return reverse_lazy('personnel_home')



#view de deconnexion
def personnel_logout(request):
    logout(request)   
    return redirect("personnel_login")


class EtudiantDetailView(DetailView):
    context_object_name = "etudiant"
    template_name = "Personnels/detail_etudiant.html"
    model = Etudiant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'ID de l'étudiant
        etudiant_id = self.object.pk
    
        photo_profil = PhotoProfil.objects.filter(etudiant=etudiant_id).last()
        
        list_cursus = Cursus.objects.filter(etudiant=etudiant_id)
        list_emploi = Emploi.objects.filter(etudiant=etudiant_id)
        list_competence = Competence.objects.filter(etudiant=etudiant_id)
        
        
        context['chemin_photo'] = photo_profil.profil.url    #2 manieres d ajout
        
        context.update({
            'list_cursus': list_cursus,
            'list_emploi': list_emploi,
            'list_competence': list_competence,
        })

        
        return context


class EtudiantDeleteView(DeleteView):
    model = Etudiant 
    template_name = "Personnels/delete_etudiant.html"
    #success_url = reverse_lazy('personnel_home')
    
    def get_success_url(self):
           return reverse_lazy('personnel_home')