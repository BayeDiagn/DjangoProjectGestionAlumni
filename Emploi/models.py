from django.db import models

from Etudiants.models import Etudiant


class Emploi(models.Model):
    entreprise=models.CharField(null=True,max_length=200)
    typecont=models.CharField(null=True,max_length=200)
    poste=models.CharField(null=True,max_length=200)
    anneedebut=models.DateField(null=True)
    anneeFin=models.DateField(null=True)
    description=models.CharField(null=True,max_length=250,blank=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.etudiant.prenom} {self.etudiant.last_name} (Emploi)"