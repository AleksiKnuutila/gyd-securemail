from django import forms

class PublicKeyForm(forms.Form):
    public_key = forms.CharField(max_length=500)
    email_address = forms.CharField(max_length=100)

""" Form for creating DataRequest """
class DataRequestForm(forms.Form):
    to_email = forms.CharField(max_length=100)

    # encrypted data blob, should contain file metadata and file
    data_blob = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
