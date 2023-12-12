from django.urls import path

from . import views

urlpatterns = [
    path("<int:user_id>/", views.emploi_home,name="emploi"),
    path("liste_emploi/<int:pk>/", views.liste_emploi, name="liste_emploi"),
    path("modifier_emploi/<int:pk>/", views.emploi_update, name="emploi_update"),
]