from django.shortcuts import render,redirect

from Etudiants.models import Etudiant
from competence.forms import CompetenceForm




def competence_home(request,user_id):
    etudiant=Etudiant.objects.get(id=user_id)
    compform=CompetenceForm()
    
    if request.method == 'POST':
        compform=CompetenceForm(request.POST)

        if compform.is_valid():  
            competence = compform.save(commit=False)           
            competence.etudiant = etudiant           
            competence.save()
            return redirect("emploi", user_id)
        
    context={"compform":compform}
    return render(request, "competence/competence_inscription.html",context)