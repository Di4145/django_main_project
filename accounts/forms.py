from django import forms
from django.contrib.auth.models import User


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


    def clean_password2(self):
        passwords = self.cleaned_data
        password1 = passwords['password1']
        password2 = passwords['password2']
        if password1 != password2:
            raise forms.ValidationError('Password dont match')
        return password1


