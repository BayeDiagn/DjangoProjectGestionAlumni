from django.urls import path
from django.contrib.auth.views import LoginView

from . import views





urlpatterns = [
    path("personnel_home", views.personnel_home, name="personnel_home"), 
    path("statistics/", views.personnel_graphic, name="personnel_graphic"),
    path("",views.PersonnelLoginView.as_view(),name="personnel_login"),
    path("personnel_logout/", views.personnel_logout, name="personnel_logout"),
    path("etudiant_detail/<int:pk>/",views.EtudiantDetailView.as_view(),name="etudiant_detail"),
    path('etudiant/<int:pk>/delete/', views.EtudiantDeleteView.as_view(), name='etudiant_delete'),
]