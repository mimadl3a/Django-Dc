from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder
from crispy_forms.helper import FormHelper
from Manager.models import Commercial
from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from captcha.fields import ReCaptchaField

    
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
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    username = forms.CharField(widget=forms.TextInput, label="Utilisateur")
    nom = forms.CharField(widget=forms.TextInput, label="Nom")
    password1 = forms.CharField(widget=forms.TextInput,label="Mot de passe", required=False)
    #password2 = forms.CharField(widget=forms.PasswordInput, label="Retapez le mot de passe")
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
        self.helper.html5_required = True

    def get_absolute_url(self):
        return reverse('indexCommercial')
    class Meta:
        model = Commercial
        fields = ['nom','username','email','password1']

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
        return user


    
    
    
    
    