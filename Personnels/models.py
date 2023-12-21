from django.db import models
from Users.models import User













class Personnel(User):
    filiere = models.CharField(max_length=200, )  
    photo = models.ImageField(upload_to='personnel/', null=True, blank=True)
    date=models.DateField(auto_now_add=True)
    
    
    
    
    
    def __str__(self):
          if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
          elif self.first_name is not None:
            return self.first_name
          else:
            return str(self.id)
   
    
    
