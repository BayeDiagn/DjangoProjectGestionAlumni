import os
from django.db import models

from Users.models import User







   

def upload_to(instance, filename):
    user_folder = f"{instance.code_permenant}_{instance.first_name}"
    if instance.cv:
        folder = f"CV_{instance.code_permenant}_{instance.first_name}" 

    #filename = instance.user.first_name + '_' + filename
    filename = user_folder + '_' + filename
    
    return os.path.join(folder, user_folder, filename)
    



class Etudiant(User):
    code_permenant=models.CharField(null=True,max_length=200,unique=True)
    adresse=models.CharField(null=True,max_length=200)
    tel=models.CharField(null=True,max_length=200)
    profession=models.CharField(null=True,max_length=200)
    niveau_actuel=models.CharField(null=True,max_length=200)
    cv=models.FileField(upload_to=upload_to, null=True, blank=True)
    about=models.TextField(null=True,max_length=250, blank=True)
    date=models.DateField(auto_now_add=True)
   
    
    
    
    def __str__(self):
          if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
          elif self.first_name is not None:
            return self.first_name
          else:
            return str(self.id)
    
    @property
    def profession_upper(self):
        return self.profession.upper()
    
    #personnaliser cette methode
    #def get_filtered_cursus(self):
     #   return self.cursus_set.filter(etablissement__in=['Universite Alioune DIOP', 'Uadb'])
     
    def get_filtered_bambey_years(self):
       return [
            {'etablissement': cursus.etablissement, 'annee_debut': cursus.annee_date_debut, 'annee_fin': cursus.annee_date_fin}
            for cursus in self.cursus_set.all()
            if 'alioune diop' in cursus.etablissement.lower() or 'uadb' in cursus.etablissement.lower()
        ]
                                                                        # if cursus.etablissement.lower() in ['universite alioune', 'uadb']]
   

    #def get_filtered_etablissements(self):
     #   from Cursus.models import Cursus
      #  cursus_contenant_alioune_diop = Cursus.objects.filter(etablissement__icontains='alioune diop').first()
       # cursus_contenant_uadb = Cursus.objects.filter(etablissement__icontains='uadb')

        #premier_cursus_alioune_diop = cursus_contenant_alioune_diop.filter(etudiant=self).first() #falcultative
        #premier_cursus_uadb = cursus_contenant_uadb.filter(etudiant=self).first()

       # if premier_cursus_alioune_diop:
        #    return premier_cursus_alioune_diop.etablissement
        #elif premier_cursus_uadb:
         #   return premier_cursus_uadb.etablissement
        #else:
         #   return None



def upload_photo_profile(instance, filename):
    user_folder = f"{instance.etudiant.code_permenant}_{instance.etudiant.first_name}"
    filename = user_folder + '_' + filename
    return os.path.join("photos_profils", user_folder, filename)

def upload_photo_couverture(instance, filename):
    user_folder = f"{instance.etudiant.code_permenant}_{instance.etudiant.first_name}"
    filename = user_folder + '_' + filename
    return os.path.join("photos_couvertures", user_folder, filename)


class PhotoProfil(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    profil = models.ImageField(upload_to=upload_photo_profile, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name} (Profil)"


class PhotoCouverture(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    couverture = models.ImageField(upload_to=upload_photo_couverture, null=True, blank=True)
    
    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name} (Couverture)"
    
    
    
