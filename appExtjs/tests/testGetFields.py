from django.test import TestCase
from django.utils import simplejson

from djangoComExtjs.appExtjs import models


class TestEditExistentObject(TestCase):
    def setUp(self):
        self.url_get_fields = '/test/get_fields/Father/'

    def testGetFieldsEditingObject(self):
        pai = models.Father.objects.create(name='Lucas')
        url = ''.join([self.url_get_fields, unicode(pai.pk)])
        expectedAnswer = 'test@test.com'
        response = self.client.get(url)
        self.assertEqual(expectedAnswer, simplejson.loads(response.content)[-1]['value'])
