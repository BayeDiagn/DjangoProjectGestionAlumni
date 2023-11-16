from django.db import models
from Etudiants.models import Etudiant

class Cursus(models.Model):
    etablissement=models.CharField(null=True,max_length=200)
    diplome_name=models.CharField(null=True,max_length=200)
    anneedebut=models.DateField(null=True)
    anneeFin=models.DateField(null=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.etudiant.prenom} {self.etudiant.last_name} (Cursus)"