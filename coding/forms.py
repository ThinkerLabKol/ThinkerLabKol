from django.forms import ModelForm
from .models import Coding

class CodingRegistrationForm(ModelForm):
    class Meta:
        model = Coding
        exclude = ('payment_id', 'paid',)