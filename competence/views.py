from django.shortcuts import render,redirect

from Etudiants.models import Etudiant
from competence.forms import CompetenceForm
from competence.models import Competence
from django.core.paginator import Paginator






def competence_home(request,user_id):
    etudiant=Etudiant.objects.get(id=user_id)
    compform=CompetenceForm()
    
    if request.method == 'POST':
        compform=CompetenceForm(request.POST)

        if compform.is_valid():  
            competence = compform.save(commit=False)           
            competence.etudiant = etudiant           
            competence.save()
            return redirect("competence", user_id)
        
    context={"compform":compform}
    return render(request, "competence/competence_inscription.html",context)



def liste_competence(request,pk):
    competence = Competence.objects.filter(etudiant=request.user.id)
    etudiant=Etudiant.objects.get(id=request.user.id)
    p=Paginator(competence,6)
    page=request.GET.get('page')
    liste=p.get_page(page)
    
    form = CompetenceForm()
    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence_add = form.save(commit=False)
            competence_add.etudiant = etudiant           
            competence_add.save()
            return redirect("liste_competence",pk)
            
    context={"form":form,"cursus": competence,"liste":liste}
    #context={"cursus":cursus}
    return render(request, "Competence/liste_competence.html",context)




def competence_update(request,pk):
    competence=Competence.objects.get(id=pk)
    form = CompetenceForm(instance=competence)
     
    if request.method == 'POST':
        form = CompetenceForm(request.POST,instance=competence)
        if form.is_valid():
            form.save()
            return redirect("liste_competence",pk)
            
    context={"form":form}
    return render(request, "Competence/competence_update.html",context)