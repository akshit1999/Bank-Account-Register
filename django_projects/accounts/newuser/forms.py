from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userForm(UserCreationForm):
    email = forms.EmailField(required = True, widget = forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = [
            'username',
            'password1',
            'password2',
            'email',
        ]

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user