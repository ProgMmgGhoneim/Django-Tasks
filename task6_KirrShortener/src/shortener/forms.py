from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .form_validation import url_validator

class KirrSubmit(forms.Form):
    Url = forms.CharField(
    max_length=200 ,
    validators =[url_validator],
    widget= forms.TimeInput(attrs={'placeholder':'Enter Long URL',
    'class':'form-control'}))

    def clean_Url(self):
        url = self.cleaned_data.get('Url')
        print(url)
        if not 'com' in url:
            raise forms.ValidationError('Not valid no .com')
        return url
