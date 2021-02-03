from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    check_box = forms.BooleanField(
        error_messages = {'required': 'You must accept the Terms and Conditions'},
        label="I agree to the Terms & Conditions and Privacy Policy."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'check_box']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'A user with that email address already exists.')
        return email
    