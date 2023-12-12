from django.urls import path

from . import views

urlpatterns = [
    path("<int:user_id>/", views.competence_home, name="competence"),
    path("liste_competence/<int:pk>/", views.liste_competence, name="liste_competence"),
    path("modifier_competence/<int:pk>/", views.competence_update, name="competence_update"),
]