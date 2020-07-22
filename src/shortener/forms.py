from django import forms
#this validator needs http:// as a part of the url.
from .validators import url_validator,dotcom_validator

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label ='Submit URL',validators = [url_validator,dotcom_validator])
