import sys
from django.db import models

TESTING = 'test' in sys.argv
if TESTING:
    class ModelTest(models.Model):
        id = models.AutoField(primary_key=True)
        field1 = models.CharField(max_length=255, unique=True,verbose_name='FiELd1')
        
    class ModelTestWithFieldsHidden(models.Model):
        id = models.AutoField(primary_key=True)
        field1 = models.CharField(max_length=255, unique=True,verbose_name='FiELd1')
        
        class Options2GridExtjs:
            name_fields_hidden = ["field1"]
            
    class ModelTestWithOrderFields(models.Model):
        id = models.AutoField(primary_key=True)
        field1 = models.CharField(max_length=255, unique=True,verbose_name='FiELd1')
        
        class Options2GridExtjs:
            name_fields_order = ['field1', 'pk']

    class ModelsWithForeignTest(models.Model):
        id = models.AutoField(primary_key=True)
        ab = models.CharField(max_length=255)
        a = models.CharField(max_length=255)
        modeltest = models.ForeignKey(ModelTest)
        
    class ModelsWithForeignWithExtraFields(models.Model):
        id = models.AutoField(primary_key=True)
        ab = models.CharField(max_length=255)
        a = models.CharField(max_length=255)
        modeltest = models.ForeignKey(ModelTest)
        
        class Options2GridExtjs:
            extra_fields = {'modeltest__field1':('Field1', 'function')}
            
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
        
    class Datas(models.Model):
        dataNascimento = models.DateField(null=True, blank=True)

        class Meta:
            ordering = ['-dataNascimento']