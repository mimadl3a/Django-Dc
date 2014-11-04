from django.forms.models import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from Commercial.models import Client, Commande
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Valider la modification'))
        self.helper.html5_required = True
        
    class Meta:
        model = Client
        fields = '__all__'
        
        
        
class CommandeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommandeForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Valider la commande'))
        self.helper.html5_required = True
        
    class Meta:
        model = Commande
        fields = '__all__'
        
        
        
        
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "login"
        self.helper.layout = Layout(
                                    Fieldset(
                                        'Authentification',
                                        'username',
                                        'Mot de passe',
                                        'password'
                                    ),
                                        ButtonHolder(
                                            Submit('submit', 'Valider'),
                                        )
                                    
                                    )
        