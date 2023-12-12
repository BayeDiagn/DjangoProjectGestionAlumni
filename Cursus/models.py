import datetime
from django.db import models
from Etudiants.models import Etudiant





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
    

cycle_name=(('Licence','Licence'),('Master','Master'),('Doctorat','Doctorat'),('Autre','Autre'))

class Cursus(models.Model):
    etablissement=models.CharField(null=True,max_length=200)
    diplome_name=models.CharField(null=True,max_length=200)
    cycle=models.CharField(null=True,max_length=200,choices=cycle_name)
    autre_cycle=models.CharField(null=True,max_length=200,blank=True)
    mois_date_debut=models.CharField(max_length=20, choices=MOIS_CHOICES)
    annee_date_debut=models.CharField(max_length=40, choices=ANNEES)
    mois_date_fin=models.CharField(max_length=20, choices=MOIS_CHOICES,null=True,blank=True)
    annee_date_fin=models.CharField(max_length=40, choices=ANNEES,null=True,blank=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name} (Cursus)"
    
    @property
    def etablissement_upper(self):
        return self.etablissement.upper()