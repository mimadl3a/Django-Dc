from django.forms.models import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from Commercial.models import Client, Commande
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms
from suit_ckeditor.widgets import CKEditorWidget
from captcha.fields import ReCaptchaField


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
            widgets = {
                'script': CKEditorWidget(editor_options={
                                'toolbar': [
                                                [
                                                  'Bold', 'Italic', 'Underline', '-', 'NumberedList', 'BulletedList',
                                                  'UIColor','NumberedList','BulletedList','-','Outdent','Indent','-'
                                                  ,'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'
                              
                                                ]
                                            ]
                                                         }),
                'objections': CKEditorWidget(editor_options={
                                'toolbar': [
                                                [
                                                  'Bold', 'Italic', 'Underline', '-', 'NumberedList', 'BulletedList',
                                                  'UIColor','NumberedList','BulletedList','-','Outdent','Indent','-'
                                                  ,'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'
                              
                                                ]
                                            ]
                                                         }),
                'plageHoraire': CKEditorWidget(editor_options={
                                'toolbar': [
                                                [
                                                  'Bold', 'Italic', 'Underline', '-', 'NumberedList', 'BulletedList',
                                                  'UIColor','NumberedList','BulletedList','-','Outdent','Indent','-'
                                                  ,'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'
                              
                                                ]
                                            ]
                                                         })
            }
            
        
    return CommandeForm
        
        
    
class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(attrs={'theme' : 'white'})
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "login"
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

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    
    
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'


        self.helper.add_input(Submit('submit', 'Submit'))







