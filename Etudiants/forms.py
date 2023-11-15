from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.password_validation import validate_password
from .models import Etudiant


class EtudiantForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm',}),
        label='',)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm',}),
        label='')
    
    #username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','autofocus': True,'placeholder':'exemple@gmail.com'}))
    
    class Meta:    #class Meta(UserCreationForm.Meta):
        model=Etudiant
        fields=["prenom","last_name","codeP","username","adresse","tel","password1","password2"]
       
        widgets ={"prenom": forms.TextInput(attrs={'class':'form-control form-control-sm ',}),
                 "last_name": forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                 "codeP": forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                 "username": forms.EmailInput(attrs={'class':'form-control form-control-sm','placeholder':'exemple@gmail.com'}),  
                 "adresse": forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                 "tel": forms.TextInput(attrs={'class':'form-control form-control-sm',}),
                 }
