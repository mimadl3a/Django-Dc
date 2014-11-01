from django.forms.models import ModelForm
from Commercial.models import Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Valider la modification'))
        self.helper.html5_required = True
        
    class Meta:
        model = Client
        fields = ['nom','prenom','code','email','adresse']
        
    