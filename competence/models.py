from django.db import models
from Etudiants.models import Etudiant

class Competence(models.Model):
    nom=models.CharField(null=True,max_length=200)
    pourcentage=models.FloatField(null=True,max_length=65)
    description=models.TextField(null=True,max_length=250,blank=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name} (Competence)"