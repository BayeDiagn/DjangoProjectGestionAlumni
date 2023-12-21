from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from . import views





urlpatterns = [
    path("etudiant_home/", views.etudiant_home, name="etudiant_home"),
    path("inscription/", views.etudiant_inscription, name="inscription"),
    
    #path("",views.etudiant_login, name="login"),
    path("",views.EtudiantLoginView.as_view(), name="login"),
    
    path("deconnexion/",views.etudiant_logout, name="deconnexion"),
    #path("deconnexion/",LogoutView.as_view(), name="deconnexion"),
    
    path("modifier/<str:pk>/",views.etudiant_update, name="update"),
    
    path("liste_etudiant/<str:pk>/",views.liste_etudiant, name="liste_etudiant"),
    path("etudiant/<str:pk>/",views.etudiant_page, name="etudiant"),
    
    path("foget_password/",views.MyPasswordRestView.as_view(),name="password_reset"),
    path("reset_password_sent/",views.MyPasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name='Etudiants/changed_password.html'),name="password_reset_confirm"),
    path("fogot_password_complete/",PasswordResetCompleteView.as_view(template_name='Etudiants/password_complet.html'),name="password_reset_complete"),

]


# path("",LoginView.as_view(template_name="Etudiants/login.html",
            #redirect_authenticated_user=True), name="login"),