from django.shortcuts import render

# Create your views here.
def personnel_home(request):
    return render(request, "etudiant_home.html")