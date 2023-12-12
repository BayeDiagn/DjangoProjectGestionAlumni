from django.shortcuts import render,redirect

from Emploi.forms import EmploiForm
from Emploi.models import Emploi
from Etudiants.models import Etudiant
from django.core.paginator import Paginator





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
            
    context={"form":form,"etudiant":etudiant}
    return render(request, "Emploi/emploi_inscription.html",context)


def liste_emploi(request,pk):
    emploi = Emploi.objects.filter(etudiant=request.user.id)
    etudiant=Etudiant.objects.get(id=request.user.id)
    p=Paginator(emploi,6)
    page=request.GET.get('page')
    liste=p.get_page(page)
    
    form = EmploiForm()
    if request.method == 'POST':
        form = EmploiForm(request.POST)
        if form.is_valid():
            emploi_add = form.save(commit=False)
            emploi_add.etudiant = etudiant           
            emploi_add.save()
            return redirect("liste_emploi",pk)
            
    context={"form":form,"emploi": emploi,"liste":liste}
    #context={"cursus":cursus}
    return render(request, "Emploi/liste_emploi.html",context)




def emploi_update(request,pk):
    emploi=Emploi.objects.get(id=pk)
    form = EmploiForm(instance=emploi)
     
    if request.method == 'POST':
        form = EmploiForm(request.POST,instance=emploi)
        if form.is_valid():
            form.save()
            return redirect("liste_emploi",pk)
            
    context={"form":form}
    return render(request, "Emploi/emploi_update.html",context)