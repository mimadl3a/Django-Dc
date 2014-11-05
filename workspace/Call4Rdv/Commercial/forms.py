from django.forms.models import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from Commercial.models import Client, Commande
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Valider la modification'))
        self.helper.html5_required = True
        
    class Meta:
        model = Client
        fields = '__all__'
        
        
def get_form_cmd(liste, *args):
    class CommandeForm(ModelForm):
        def __init__(self, *args, **kwargs):
            super(CommandeForm,self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit('submit', 'Valider la commande'))
            self.helper.html5_required = True
            
        class Meta:
            model = Commande
            #fields = ['code','dateCommande','dateReglement']
            fields = '__all__'
            exclude = liste
        
    return CommandeForm
        
        
    
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

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'


        self.helper.add_input(Submit('submit', 'Submit'))







