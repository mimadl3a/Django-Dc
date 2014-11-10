from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from Manager.models import Commercial


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
        exclude = ['password','last_login','is_superuser','groups','is_staff','date_joined']
        
        
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_input(Submit('submit', 'Valider'))
        self.helper.html5_required = True
    
    class Meta:
        model = Commercial
        fields = "__all__"
        exclude = ['password','last_login','is_superuser','groups','is_staff','date_joined']
        