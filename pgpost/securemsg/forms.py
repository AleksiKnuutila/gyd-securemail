from django import forms

class PublicKeyForm(forms.Form):
    public_key = forms.CharField(max_length=500)
    email_address = forms.CharField(max_length=100)
