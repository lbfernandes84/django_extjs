from django.test import TestCase
from django.utils import simplejson
from django.test.client import Client
import datetime

import json2Extjs
import models
import views

class ModelsTest(TestCase):
    def setUp(self):
        self.collumns2grid_extjs = views.Collumns2GridExtjs()

    def test_collumns_model2grid_extjs(self):
        model = models.ModelTest()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'FiELd1', 'dataIndex':'field1', 'flex':1, 'filter':{'type':'string'}})
        collumns = simplejson.dumps(collumns)
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(self.collumns2grid_extjs.output_extjs(model)))
        
    def test_collumns_model2grid_extjs_with_fields_order(self):
        model = models.ModelTestWithOrderFields()
        collumns = []
        collumns.append({'header':'FiELd1', 'dataIndex':'field1', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns = simplejson.dumps(collumns)
        collumns2grid_extjs = views.Collumns2GridExtjs()
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(collumns2grid_extjs.output_extjs(model)))
        
    def test_collumns_model2grid_extjs_with_field_hidden(self):
        model = models.ModelTestWithFieldsHidden()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'FiELd1', 'dataIndex':'field1', 'hidden':True, 'flex':1, 'filter':{'type':'string'}})
        collumns = simplejson.dumps(collumns)
        collumns2grid_extjs = views.Collumns2GridExtjs()
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(collumns2grid_extjs.output_extjs(model)))
        
    def test_collumns_model2grid_extjs_with_field_data_filter(self):
        model = models.Datas()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'dataNascimento', 'dataIndex':'dataNascimento', 'flex':1, 'filter':{'type':'date'}})
        collumns = simplejson.dumps(collumns)
        collumns2grid_extjs = views.Collumns2GridExtjs()
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(collumns2grid_extjs.output_extjs(model)))
        

class ModelsWithForeignTest(TestCase):
    def setUp(self):
        self.collumns2grid_extjs = views.Collumns2GridExtjs()

    def test_collumns_model2grid_extjs(self):
        model = models.ModelsWithForeignTest()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'Ab', 'dataIndex':'ab', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'A', 'dataIndex':'a', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'Modeltest', 'dataIndex':'modeltest', 'flex':1, 'filter':{'type':'string'}, 'hidden':True})
        collumns = simplejson.dumps(collumns)
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(self.collumns2grid_extjs.output_extjs(model)))

    def test_collumns_model2grid_extjs_with_foreign_hidden(self):
        collumns2grid_extjs = views.Collumns2GridExtjs()
        model = models.ModelsWithForeignTest()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'Ab', 'dataIndex':'ab', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'A', 'dataIndex':'a', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'Modeltest', 'dataIndex':'modeltest', 'flex':1, 'filter':{'type':'string'}, 'hidden':True})
        collumns = simplejson.dumps(collumns)
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(collumns2grid_extjs.output_extjs(model)))
        
    def test_collumns_model2grid_extjs_with_extra_fields(self):
        model = models.ModelsWithForeignWithExtraFields()
        collumns = []
        collumns.append({'header':'Id', 'dataIndex':'pk', 'hidden':True, 'flex':1, 'filter':{'type':'numeric'}})
        collumns.append({'header':'Ab', 'dataIndex':'ab', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'A', 'dataIndex':'a', 'flex':1, 'filter':{'type':'string'}})
        collumns.append({'header':'Modeltest', 'dataIndex':'modeltest', 'flex':1, 'filter':{'type':'string'}, 'hidden':True})
        collumns.append({'header':'Field1', 'dataIndex':'modeltest__field1', 'flex':1, 'filter':{'type':'string'}})
        collumns = simplejson.dumps(collumns)
        collumns2grid_extjs = views.Collumns2GridExtjs()
        self.assertListEqual(simplejson.loads(collumns), simplejson.loads(collumns2grid_extjs.output_extjs(model)))

class json2ExtjsTest(TestCase):
    def test_serialiser(self):
        modelTest1 = models.Father(name='Father1')
        modelTest1.save()
        modelTest2 = models.Father(name='Father2')
        modelTest2.save()
        data = []
        data.append({'name':modelTest1.name, 'pk':modelTest1.id})
        data.append({'name':modelTest2.name, 'pk':modelTest2.id})
        data = simplejson.dumps(data)
        data_json2Extjs = json2Extjs.ExtJSONSerialiser().serialize(models.Father.objects.all())
        self.assertEqual(data, data_json2Extjs)
        
    def test_serialiser_with_inherited_class(self):
        modelTest1 = models.GrandFather(name='vovo1', age=80)
        modelTest1.save()
        modelTest2 = models.GrandFather(name='vovo2', age=95)
        modelTest2.save()
        data = []
        data.append({'name':modelTest1.name, 'pk':modelTest1.id, 'age':80})
        data.append({'name':modelTest2.name, 'pk':modelTest2.id, 'age':95})
        data = simplejson.dumps(data)
        data_json2Extjs = json2Extjs.ExtJSONSerialiser().serialize(models.GrandFather.objects.all())
        self.assertEqual(data, data_json2Extjs)
        
    def test_serializer_with_foreignkey_field_empty_field(self):
        modelTest = models.ForTestsForeignKey(name='Name teste')
        modelTest.save()
        data_json2Extjs = json2Extjs.ExtJSONSerialiser()
        result = json2Extjs.ExtJSONSerialiser().serialize(models.ForTestsForeignKey.objects.all())
        resultExpected = simplejson.dumps([{"pk": 1, "name": "Name teste", "foreignKeyField": None}])
        self.assertItemsEqual(resultExpected, result)
        
    def test_serializer_with_foreignkey_field_not_empty_field(self):
        father = models.Father(name='father')
        father.save()
        modelTest = models.ForTestsForeignKey(name='Name teste', foreignKeyField=father)
        modelTest.save()
        result = json2Extjs.ExtJSONSerialiser().serialize(models.ForTestsForeignKey.objects.all())
        resultExpected = simplejson.dumps([{"pk": 1, "name": "Name teste", "foreignKeyField": father.id}])
        self.assertEqual(resultExpected, result)

class TestLoadGrid(TestCase):
    def setUp(self):
        self.fatherA = models.Father.objects.create(name='a')
        self.fatherB = models.Father.objects.create(name='b')
        self.base_load_grid_url = '/gridExtjs/load_model_in_grid_extjs/gridExtjs/'

    def test_get_all_register_not_sorted(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/')
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize(models.Father.objects.all())
        self.assertEqual(expect_answer, response.content)
        
    def test_get_all_register_order_by_name_asc(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'sort': '[{"property":"name", "direction":"ASC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherA, self.fatherB])
        self.assertEqual(expect_answer, response.content)
        
    def test_get_all_register_order_by_name_desc(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'sort': '[{"property":"name", "direction":"DESC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherB, self.fatherA])
        self.assertEqual(expect_answer, response.content)
        
    def test_get_all_register_order_by_field1_desc_and_field2_asc(self):
        grandFatherA = models.GrandFather.objects.create(name = 'a', age = 2)
        grandFatherB = models.GrandFather.objects.create(name = 'a', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'sort': '[{"property":"name", "direction":"DESC"}, {"property":"age", "direction":"ASC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB, grandFatherA])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_by_string(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'A', 'filter[0][field]': 'name'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherA])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_string_and_one_field_int(self):
        grandFatherA = models.GrandFather.objects.create(name = 'b', age = 10)
        grandFatherB = models.GrandFather.objects.create(name = 'b', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'B', 'filter[0][field]': 'name',
                                                          'filter[1][data][type]': 'numeric', 'filter[1][data][value]': '1', 'filter[1][field]': 'age', 'filter[1][data][comparison]': 'eq'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_int_greater_than(self):
        grandFatherA = models.GrandFather.objects.create(name = 'b', age = 10)
        grandFatherB = models.GrandFather.objects.create(name = 'a', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'numeric', 'filter[0][data][value]': '1', 'filter[0][field]': 'age', 'filter[0][data][comparison]': 'gt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherA])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_int_less_than(self):
        grandFatherA = models.GrandFather.objects.create(name = 'b', age = 10)
        grandFatherB = models.GrandFather.objects.create(name = 'a', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'numeric', 'filter[0][data][value]': '10', 'filter[0][field]': 'age', 'filter[0][data][comparison]': 'lt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_date_equal(self):
        datasA = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '20/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'eq'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasA])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_date_greater_than(self):
        datasA = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '20/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'gt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasB])
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_one_field_date_less_than(self):
        datasA = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '21/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'lt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasA])
        self.assertEqual(expect_answer, response.content)
        
    def test_get_page1(self):
        grandFatherA = models.GrandFather.objects.create(name = 'b', age = 10)
        grandFatherB = models.GrandFather.objects.create(name = 'a', age = 1)
        grandFatherC = models.GrandFather.objects.create(name = 'c', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'limit': '2', 'start': '0', 'page': '1'})
        expect_answer = simplejson.dumps({'total': '3', "register": [
                                                               {"pk": grandFatherA.pk, "age": grandFatherA.age, "name": grandFatherA.name},
                                                               {"pk": grandFatherB.pk, "age": grandFatherB.age, "name": grandFatherB.name},
                                                               ]})
        self.assertEqual(expect_answer, response.content)
        
    def test_get_page2(self):
        grandFatherA = models.GrandFather.objects.create(name = 'b', age = 10)
        grandFatherB = models.GrandFather.objects.create(name = 'a', age = 1)
        grandFatherC = models.GrandFather.objects.create(name = 'c', age = 1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'limit': '2', 'start': '2', 'page': '2'})
        expect_answer = simplejson.dumps({'total': '3', "register": [{"pk": grandFatherC.pk, "age": grandFatherC.age, "name": grandFatherC.name}]})
        self.assertEqual(expect_answer, response.content)
        
    def test_filter_with_foreign(self):
        forTestsForeignKey1 = models.ForTestsForeignKey.objects.create(name = 'ForTestsForeignKey1', foreignKeyField = self.fatherA)
        forTestsForeignKey2 = models.ForTestsForeignKey.objects.create(name = 'ForTestsForeignKey2', foreignKeyField = self.fatherB)
        c = Client()
        response = c.get(self.base_load_grid_url + 'ForTestsForeignKey/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'a', 'filter[0][field]': 'foreignKeyField__name'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([forTestsForeignKey1])
        self.assertEqual(expect_answer, response.content)
        
    def test_order_with_parameters_of_model(self):
        datasA = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento = datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/')
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasB, datasA])
        self.assertEqual(expect_answer, response.content)