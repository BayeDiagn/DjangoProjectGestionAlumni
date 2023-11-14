from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("home/", views.etudiant_home, name="etudiant_home"),
    path("inscription/", views.etudiant_inscription, name="inscription"),
    path("",LoginView.as_view(template_name="Etudiants/login.html",
            redirect_authenticated_user=True), name="login"),
    path("deconnexion/",views.etudiant_logout, name="logout"),
]