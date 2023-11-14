from django.shortcuts import render

# Create your views here.
def emploi_home(request):
    return render(request, "etudiant_home.html")