from django.urls import path

from . import views

urlpatterns = [
    path("<int:user_id>/", views.emploi_home,name="emploi"),
]