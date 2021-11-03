from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.forms import ModelForm, widgets, Textarea, TextInput, CharField
from django import forms


class MyMinimumLengthValidator(MinimumLengthValidator):

    def __init__(self, min_length=2):
        super().__init__(min_length)
        self.min_length = min_length


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': TextInput(attrs={'class': "form-control"})
        }

    password1 = forms.CharField(
        label="Password",
        strip=False,
        help_text=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "form-control"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "form-control"}),
        strip=False,
    )


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': "form-control"}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': "form-control"}),
    )
