from django import forms
from .models import Cursus



class CursusForm(forms.ModelForm):
    
    class Meta:
        model = Cursus
        fields =['etablissement','diplome_name','anneedebut','anneeFin']
       
        widgets ={"etablissement": forms.TextInput(attrs={'class':'form-control form-control-sm ',}),
                 "diplome_name": forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                 "anneedebut": forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}, format='%Y-%m-%d'),
                 "anneeFin": forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}, format='%d-%m-%y'),
                 }
 