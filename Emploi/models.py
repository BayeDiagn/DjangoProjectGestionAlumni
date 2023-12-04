from django.db import models

from Etudiants.models import Etudiant
from calendar import month_name
import datetime





#MOIS = list(month_name)
#MOIS_CHOICES = []

#for num, mois in enumerate(MOIS):
    #MOIS_CHOICES.append((str(num+1), mois))
    
#print(MOIS_CHOICES)


MOIS_CHOICES = [
    ('1', 'Janvier'),
    ('2', 'Février'),
    ('3', 'Mars'), 
    ('4', 'Avril'),
    ('5', 'Mai'),
    ('6', 'Juin'),
    ('7', 'Juillet'),
    ('8', 'Août'),
    ('9', 'Septembre'),
    ('10', 'Octobre'),
    ('11', 'Novembre'),
    ('12', 'Décembre'),
]


start_year = 2007
end_year = datetime.date.today().year

ANNEES = []
for annee in range(start_year, end_year+8):
    ANNEES.append((str(annee), str(annee)))
    
#print(ANNEES)



class Emploi(models.Model):
    entreprise=models.CharField(null=True,max_length=200)
    typecont=models.CharField(null=True,max_length=200)
    poste=models.CharField(null=True,max_length=200)
    mois_date_debut=models.CharField(max_length=20, choices=MOIS_CHOICES)
    annee_date_debut=models.CharField(max_length=40, choices=ANNEES)
    mois_date_fin=models.CharField(max_length=20, choices=MOIS_CHOICES,null=True,blank=True)
    annee_date_fin=models.CharField(max_length=40, choices=ANNEES,null=True,blank=True)
    description=models.TextField(null=True,max_length=250,blank=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name} (Emploi)"