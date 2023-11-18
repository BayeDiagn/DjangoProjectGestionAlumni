from django import forms
from .models import Competence



class CompetenceForm(forms.ModelForm):
    
    class Meta:
        model = Competence
        fields =['nom','pourcentage','description']
       
        



        
 