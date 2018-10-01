from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def url_validator(value):
    try:
        URLValidator(value)
    except:
        raise ValidationError('Not valid enter the url like that http://www.google.com')
    return value
