"""
Definition of forms.
"""
from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('FirstName','LastName','Email')

class ContactForm1(forms.Form):
    cid = forms.CharField(max_length=5,initial='0',widget=forms.HiddenInput())
   
    firstname = forms.CharField(max_length=50, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    mobileno = forms.CharField(max_length=15,widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Mobile No'}))

