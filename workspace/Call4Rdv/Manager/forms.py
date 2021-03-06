from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder
from crispy_forms.helper import FormHelper
from Manager.models import Commercial, DataCommercial
from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from captcha.fields import ReCaptchaField
import csv
from django.db import connection

    
class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(attrs={'theme' : 'white'})
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "Managerlogin"
        self.helper.layout = Layout(
                                    Fieldset(
                                        'Authentification',
                                        'username',
                                        'password',
                                        'captcha',
                                    ),
                                        ButtonHolder(
                                            Submit('submit', 'Valider'),
                                        )
                                    
                                    )

class CommercialForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CommercialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
        self.helper.html5_required = True
    class Meta:
        model = Commercial
        fields = "__all__"
        exclude = ['user_permissions','password','last_login','is_superuser','groups','is_staff','date_joined', 'password1','password2']


class CommercialUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommercialUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
    class Meta:
        model = Commercial
        fields = "__all__"
        exclude = ['user_permissions','last_login','is_superuser','groups','is_staff','date_joined']


""" 
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
    
    class Meta:
        model = Commercial
        fields = "__all__"
        exclude = ['user_permissions','password','last_login','is_superuser','groups','is_staff','date_joined', 'password1','password2']
"""
class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    nom = forms.CharField(widget=forms.TextInput, label="Nom", help_text='Ceci est un help text')
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    username = forms.CharField(widget=forms.TextInput, label="Utilisateur")
    password1 = forms.CharField(widget=forms.TextInput,label="Mot de passe", required=False)
    
    def __init__(self, *args, **kwargs):
        """initial = kwargs.get('initial', {})
        initial['nom'] = 'initial_name'
        kwargs['initial'] = initial"""
        
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
        self.helper.html5_required = True
        

    def get_absolute_url(self):
        return reverse('indexCommercial')
    class Meta:
        model = Commercial
        fields = ['data','nom','username','email','password1']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if 'password1' in self.cleaned_data and self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            records = csv.reader(self.cleaned_data["data"],delimiter=';')
            cursor = connection.cursor()
            for line in records:
                Civ         = line[0]
                Nom         = line[1]
                Prenom      = line[2]
                Adresse1    = line[3]
                Adresse2    = line[4]
                Adresse3    = line[5]
                Adresse4    = line[6]
                Cp          = line[7]
                Ville       = line[8]
                Email       = line[9]
                cursor.execute("INSERT INTO Manager_datacommercial VALUES(null"
                                ",'"+Civ+"'"
                                ",'"+Nom+"'"
                                ",'"+Prenom+"'"
                                ",'"+Adresse1+"'"
                                ",'"+Adresse2+"'"
                                ",'"+Adresse3+"'"
                                ",'"+Adresse4+"'"
                                ",'"+Cp+"'"
                                ",'"+Ville+"'"
                                ",'"+Email+"'"
                                +")")
                """d = DataCommercial(Civ = line[0],Nom = line[1],Prenom = line[2],Adresse1 = line[3],
                                   Adresse2 = line[4],
                                   Adresse3 = line[5],
                                   Adresse4 = line[6],
                                   Cp = line[7],
                                   Ville = line[8],
                                   Email = line[9])
                d.save()"""
        return user


    
    
    
    
    