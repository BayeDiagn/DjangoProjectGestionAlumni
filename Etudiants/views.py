from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from Etudiants.forms import EtudiantForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import LogoutView




@login_required
def etudiant_home(request):
    return render(request, "Etudiants/etudiant_home.html")


#view d'inscription
def etudiant_inscription(request):
    form = EtudiantForm()
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    context={"form":form}
    return render(request, "Etudiants/inscription.html",context)


#view de connexion
def etudiant_login(request):
    message=" "
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("etudiant_home")
            
            #message = f'Bonjour, {user.prenom} Vous êtes connecté.'
        else:
            message = 'Identifiants invalides.'
                
    context={"message":message}
    return render(request, "Etudiants/login.html",context)


#view de deconnexion
def etudiant_logout(request):
    logout(request)
    return redirect("login")
