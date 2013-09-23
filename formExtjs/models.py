import sys
from django.db import models

TESTING = 'test' in sys.argv
if TESTING:
    class ModeloParaTesteTT(models.Model):
        boolean_field = models.BooleanField(default=False)
        boolean_field1 = models.BooleanField(verbose_name='BFTeste', default=True)
        char_field = models.CharField(max_length=10)
        decimal_field = models.DecimalField(decimal_places=3, max_digits=6)
        email_field = models.EmailField()
        float_field = models.FloatField()
        integer_field = models.IntegerField()
        url_field = models.URLField()
        ip_address_field = models.IPAddressField()
        generic_ip_address_field = models.GenericIPAddressField()
        date_field = models.DateField()
        time_field = models.TimeField()
        slug_field = models.SlugField()
        file_path_field = models.FilePathField()
        null_boolean_field = models.NullBooleanField()
        date_time_field = models.DateTimeField()

    class Father(models.Model):
        name = models.CharField(max_length=10)

    class Child(models.Model):
        name = models.CharField(max_length=10)
        father = models.ForeignKey(Father)

    class CharFieldWithChoices(models.Model):
        name = models.CharField(max_length=10, choices=((1, 'Um'), (2, 'Dois')))

    class Poll(models.Model):
        question = models.CharField(max_length=200)
    
    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice = models.CharField(max_length=200)
