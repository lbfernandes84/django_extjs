from django.db.models import CASCADE, PROTECT, SET_NULL
from django.db import models
import sys

TESTING = 'test' in sys.argv
if TESTING:
    class Father(models.Model):
        name = models.CharField(max_length=20)

        def __unicode__(self):
            return self.name

    class James(models.Model):
        name = models.CharField(max_length=20)

    class GrandFather(James):
        age = models.IntegerField()
        
        class Options2GridExtjs:
            extra_fields = {'name':('Name', 'name')}

    class ForTestsForeignKey(models.Model):
        name = models.CharField(max_length=20)
        foreignKeyField = models.ForeignKey(Father, null=True, blank=True)

    class ModelOnDelete(models.Model):
        name = models.CharField(max_length=20)
        foreignKeyFieldProtect = models.ForeignKey(Father, on_delete=PROTECT, related_name='protect', null=True, blank=True)
        foreignKeyFieldCascade = models.ForeignKey(Father, on_delete=CASCADE, related_name='cascade', null=True, blank=True)
        foreignKeyFieldSetNull = models.ForeignKey(Father, on_delete=SET_NULL, null=True, blank=True)

    class Datas(models.Model):
        dataNascimento = models.DateField(null=True, blank=True)

        class Meta:
            ordering = ['-dataNascimento']
