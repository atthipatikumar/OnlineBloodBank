from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import Donarlist


class UserForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'custom-form',
        }))

    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={
        'class': 'custom-form',
    }))


class DonateModelForm(ModelForm):
    class Meta:
        model = Donarlist
        fields = ['BloodGroup', 'name', 'addrees', 'cellNO', 'pic']