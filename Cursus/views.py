from django.shortcuts import render,redirect

from Cursus.forms import CursusForm
from Etudiants.models import Etudiant





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