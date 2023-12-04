from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views

urlpatterns = [
    path("home/", views.etudiant_home, name="etudiant_home"),
    path("inscription/", views.etudiant_inscription, name="inscription"),
    
    #path("",views.etudiant_login, name="login"),
    path("",LoginView.as_view(template_name="Etudiants/login.html",
            redirect_authenticated_user=True), name="login"),
    
    path("deconnexion/",views.etudiant_logout, name="deconnexion"),
    #path("deconnexion/",LogoutView.as_view(), name="deconnexion"),
    
    path("modifier/<str:pk>/",views.etudiant_update, name="update"),
]


# path("",LoginView.as_view(template_name="Etudiants/login.html",
            #redirect_authenticated_user=True), name="login"),