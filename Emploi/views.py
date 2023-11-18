from django.shortcuts import render,redirect

from Emploi.forms import EmploiForm
from Etudiants.models import Etudiant





def emploi_home(request,user_id):
    etudiant=Etudiant.objects.get(id=user_id)
    form = EmploiForm()
    #compform=CompetenceForm()
    
    if request.method == 'POST':
        form = EmploiForm(request.POST)
        #compform=CompetenceForm(request.POST)
        if form.is_valid():
            emploi = form.save(commit=False)
            emploi.etudiant = etudiant
            emploi.save()
            return redirect("emploi", user_id)
        #if compform.is_valid():  
         #   competence = compform.save(commit=False)           
          #  competence.etudiant = etudiant           
           # competence.save()
            #return redirect("emploi", user_id)        
            
    context={"form":form,"etudiant":etudiant}
    return render(request, "Emploi/emploi_inscription.html",context)