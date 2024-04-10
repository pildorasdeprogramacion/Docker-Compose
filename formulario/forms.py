from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'email', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


