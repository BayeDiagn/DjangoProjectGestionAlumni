from django.shortcuts import render,redirect

from Cursus.forms import CursusForm
from Cursus.models import Cursus
from Etudiants.models import Etudiant
from django.core.paginator import Paginator





def cursus_home(request,user_id):
    etudiant=Etudiant.objects.get(id=user_id)
    form = CursusForm()
     
    if request.method == 'POST':
        form = CursusForm(request.POST)
        if form.is_valid():
            cursus = form.save(commit=False)
            cursus.etudiant = etudiant           
            cursus.save()
            return redirect("cursus", user_id)
            
    context={"form":form,"etudiant": etudiant}
    return render(request, "Cursus/cursus_inscription.html",context)




def liste_cursus(request,pk):
    cursus = Cursus.objects.filter(etudiant=request.user.id)
    etudiant=Etudiant.objects.get(id=request.user.id)
    p=Paginator(cursus,6)
    page=request.GET.get('page')
    liste=p.get_page(page)
    
    form = CursusForm()
    if request.method == 'POST':
        form = CursusForm(request.POST)
        if form.is_valid():
            cursus_add = form.save(commit=False)
            cursus_add.etudiant = etudiant           
            cursus_add.save()
            return redirect("liste_cursus",pk)
            
    context={"form":form,"cursus": cursus,"liste":liste}
    #context={"cursus":cursus}
    return render(request, "Cursus/liste_cursus.html",context)




def cursus_update(request,pk):
    cursus=Cursus.objects.get(id=pk)
    form = CursusForm(instance=cursus)
     
    if request.method == 'POST':
        form = CursusForm(request.POST,instance=cursus)
        if form.is_valid():
            form.save()
            return redirect("liste_cursus",pk)
            
    context={"form":form}
    return render(request, "Cursus/cursus_update.html",context)