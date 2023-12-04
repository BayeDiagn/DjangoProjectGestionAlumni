from django.urls import path

from Cursus import views

urlpatterns = [
    path("<int:user_id>/", views.cursus_home, name="cursus"),
    path("liste_cursus/<int:pk>/", views.liste_cursus, name="liste_cursus"),
    path("modifier_cursus/<int:pk>/", views.cursus_update, name="cursus_update"),
]