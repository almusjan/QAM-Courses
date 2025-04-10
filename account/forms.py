from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='البريد الإلكتروني')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("البريد الالكتروني مستخدم")
        return email





