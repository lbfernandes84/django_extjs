from django.forms.models import ModelForm
from django.forms.fields import EmailField
import sys

import models

TESTING = 'test' in sys.argv
if TESTING:
    class Father(ModelForm):
        email = EmailField(required=False)

        def __init__(self, *args, **kwargs):
            super(Father, self).__init__(*args, **kwargs)
            self.fields['email'].initial = 'test@test.com'

        class Meta:
            model = models.Father
