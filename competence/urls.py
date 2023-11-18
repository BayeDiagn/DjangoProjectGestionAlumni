from django.urls import path

from . import views

urlpatterns = [
    path("<int:user_id>/", views.competence_home, name="competence"),
]