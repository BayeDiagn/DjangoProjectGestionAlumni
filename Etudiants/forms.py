from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
#from django.forms import ModelForm
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
        
        

#class LoginForm(forms.Form):
 #   email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','autofocus': True,'placeholder':'exemple@gmail.com'}))
  #  password = forms.CharField(
   #     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm',}),
    #    label='',)
    
    
    #def clean_password(self):
        # Récupérer la valeur du champ password
       # password = self.cleaned_data.get('mot_de_passe')

        # Valider le mot de passe en utilisant les validateurs définis dans les paramètres
       # try:
           # validate_password(password, user=self.instance)
        #except forms.ValidationError as error:
            #self.add_error('password', error)

        # Retourner la valeur nettoyée
       # return password
    
    
    #def clean_password_confirm(self):
        # Récupérer la valeur du champ password
       # password = self.cleaned_data.get('mot_de_passe')

        # Récupérer la valeur du champ password_confirm
       # password_confirm = self.cleaned_data.get('mot_de_passe_de_confirmation')

        # Valider que password et password_confirm sont égaux
        #if password and password_confirm and password != password_confirm:
           # raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        # Retourner la valeur nettoyée
       # return password_confirm
