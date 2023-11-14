from django.contrib.auth.models import AbstractUser
from django.db import models



class Etudiant(AbstractUser):
    prenom=models.CharField(null=True,max_length=200)
    username = models.EmailField(unique=True)
    codeP=models.CharField(null=True,max_length=200,unique=True)
    adresse=models.CharField(null=True,max_length=200)
    tel=models.CharField(null=True,max_length=200)
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    date=models.DateField(auto_now_add=True)
   
    first_name = None
    
    #USERNAME_FIELD = 'email'  
    #EMAIL_FIELD = 'username'  
    #REQUIRED_FIELDS=[]
    
    
    
    def __str__(self):
       if self.prenom is not None and self.last_name is not None:
            return f"{self.prenom} {self.last_name}"
       elif self.username is not None:
            return self.username
       elif self.last_name is not None:
            return self.last_name
       else:
            return str(self.id)
