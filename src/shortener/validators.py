from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
def url_validator(url):
	url_validator = URLValidator()
	try:
		url_validator(url)
	except:
		raise ValidationError('invalid url')
	return url

def dotcom_validator(url):
	if '.com' not in url:
		raise ValidationError('invalid url no .com')
	return url	
