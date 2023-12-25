from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager







class UserManager(BaseUserManager):
     
     def create_user(self, email, password=None, **extra_fields):
            if not email: 
               raise ValueError('L\'adresse email est obligatoire.')

            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
     def create_superuser(self, email, password=None, **extra_fields):
        
        # Crée le superuser    
        user = self.create_user(email, password, **extra_fields)  
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        return user




class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin=models.BooleanField(default=False)
    is_etudiant=models.BooleanField(default=True)
    is_personnel=models.BooleanField(default=False)
    
    
    
    username = None
    
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name', 'last_name']
    #REQUIRED_FIELDS = []

    
    objects = UserManager()
    
    def __str__(self):
          if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
          elif self.first_name is not None:
            return self.first_name
          else:
            return str(self.id)