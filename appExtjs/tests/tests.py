  # -*- encoding: utf-8 -*-
import datetime
from django.test import TestCase
from django.test.client import Client
from django.utils import simplejson
from mocker import Mocker

from appExtjs import models, structure2Extjs, views
from gridExtjs import json2Extjs


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
        self.assertItemsEqual(eval(data), eval(data_json2Extjs))

    def test_serialiserWithInheritedClass(self):
        modelTest1 = models.GrandFather(name='vovo1', age=80)
        modelTest1.save()
        modelTest2 = models.GrandFather(name='vovo2', age=95)
        modelTest2.save()
        data = []
        data.append({'name':modelTest1.name, 'pk':modelTest1.id, 'age':80})
        data.append({'name':modelTest2.name, 'pk':modelTest2.id, 'age':95})
        data = simplejson.dumps(data)
        result = json2Extjs.ExtJSONSerialiser().serialize(models.GrandFather.objects.all())
        self.assertEqual(data, result)

    def test_serializerWithForeignKeyFieldEmptyField(self):
        modelTest = models.ForTestsForeignKey(name='Name teste')
        modelTest.save()
        result = json2Extjs.ExtJSONSerialiser().serialize(models.ForTestsForeignKey.objects.all())
        resultExpected = [{"pk": modelTest.pk, "name": "Name teste", "foreignKeyField": None}]
        resultExpected = simplejson.dumps(resultExpected)
        self.assertEqual(resultExpected, result)

    def test_serializerWithForeignKeyFieldNotEmptyField(self):
        father = models.Father(name='father')
        father.save()
        modelTest = models.ForTestsForeignKey(name='Name teste', foreignKeyField=father)
        modelTest.save()
        result = json2Extjs.ExtJSONSerialiser().serialize(models.ForTestsForeignKey.objects.all())
        resultExpected = [{"pk": 1, "name": "Name teste", "foreignKeyField": father.id}]
        resultExpected = simplejson.dumps(resultExpected)
        self.assertEqual(resultExpected, result)

class Item_MenuTest(TestCase):
    def test_item_menu2dict(self):
        item_menu = structure2Extjs.Item_Menu('text', 'action', 'title_window_list', 'url_get_collumns', 'url_load_grid', 'url_delete_record',
            'title_window_form', 'url_get_fields', 'url_save_record')
        dict_item_menu_expected = {'text':'text', 'action': 'action', 'cls':'textItemMenu', 'window_configuration':{
            'list':{'title':'title_window_list', 'report_url': '', 'get_columns':'url_get_collumns', 'url_load_grid':'url_load_grid', 'delete_record':'url_delete_record', 'report_button_hidden': True},
            'form':{'title':'title_window_form', 'get_fields':'url_get_fields', 'save_record':'url_save_record'}}}
        self.assertDictEqual(dict_item_menu_expected, item_menu.item_menu2dict())


class MenuTest(TestCase):
    def test_menu2dict_with_one_item_menu(self):
        item_menu = structure2Extjs.Item_Menu('text', 'action', 'title_window_list', 'url_get_collumns', 'url_load_grid', 'url_delete_record',
            'title_window_form', 'url_get_fields', 'url_save_record')
        menu_expected = {'text':'File', 'cls':'FileMenu' , 'menu':{'items':[{'text':'text', 'cls':'textItemMenu' , 'action': 'action', 'window_configuration':{
            'list':{'title':'title_window_list', 'report_url': '', 'get_columns':'url_get_collumns', 'url_load_grid':'url_load_grid', 'delete_record':'url_delete_record', 'report_button_hidden': True},
            'form':{'title':'title_window_form', 'get_fields':'url_get_fields', 'save_record':'url_save_record'}}}]}}
        menu = structure2Extjs.Menu('File', [item_menu])
        self.assertDictEqual(menu_expected, menu.menu2dict())

    def test_menu2dict_with_two_item_menu(self):
        item_menu1 = structure2Extjs.Item_Menu('text1', 'action1', 'title_window_list1', 'url_get_collumns1', 'url_load_grid', 'url_delete_record1',
            'title_window_form1', 'url_get_fields1', 'url_save_record1')
        item_menu2 = structure2Extjs.Item_Menu('text2', 'action2', 'title_window_list2', 'url_get_collumns2', 'url_load_grid', 'url_delete_record2',
            'title_window_form2', 'url_get_fields2', 'url_save_record2')
        menu_expected = {'text':'File', 'cls':'FileMenu' , 'menu':{'items':[{'text':'text1', 'action': 'action1', 'cls':'text1ItemMenu', 'window_configuration':{
            'list':{'title':'title_window_list1', 'report_url': '', 'get_columns':'url_get_collumns1', 'url_load_grid':'url_load_grid', 'delete_record':'url_delete_record1', 'report_button_hidden': True},
            'form':{'title':'title_window_form1', 'get_fields':'url_get_fields1', 'save_record':'url_save_record1'}}},
            {'text':'text2', 'action': 'action2', 'cls':'text2ItemMenu', 'window_configuration':{
            'list':{'title':'title_window_list2', 'report_url': '', 'get_columns':'url_get_collumns2', 'url_load_grid':'url_load_grid', 'delete_record':'url_delete_record2', 'report_button_hidden': True},
            'form':{'title':'title_window_form2', 'get_fields':'url_get_fields2', 'save_record':'url_save_record2'}}}]}}
        menu = structure2Extjs.Menu('File', [item_menu1, item_menu2])
        self.assertDictEqual(menu_expected, menu.menu2dict())


class TestButton(TestCase):
    def test_button2dict(self):
        button_action_expected = 'add'
        button_configuration_expect = {'label':'Add', 'cls':'AddButton' , 'path_image':'images/add.png', 'tooltip':'Help Message'}
        button = structure2Extjs.Button(button_action_expected, 'Add', 'images/add.png', 'Help Message')
        self.assertDictEqual({button_action_expected:button_configuration_expect}, button.button2dict())

class TestAction(TestCase):
    def test_action2dict(self):
        action_expected = 'delete'
        action_configuration_expect = {'title':'Delete', 'msg':'Delete?'}
        action = structure2Extjs.Action(action_expected, 'Delete', 'Delete?')
        self.assertDictEqual({action_expected:action_configuration_expect}, action.action2dict())

class TestAjax(TestCase):
    def test_ajax2dict(self):
        ajax = {'failure':{'title':'Erro', 'msg':'Mensagem'}}
        ajax_expected = 'failure'
        ajax_configuration_expect = {'title':'Erro', 'msg':'Mensagem'}
        ajax = structure2Extjs.Ajax(ajax_expected, 'Erro', 'Mensagem')
        self.assertDictEqual({ajax_expected:ajax_configuration_expect}, ajax.ajax2dict())


class TestConfiguration_Initial(TestCase):
    def test_Configuration_Initial2dict(self):
        self.maxDiff = None
        configuration_initial_expected = {"success": True}
        configuration_initial_expected['application'] = {'title':'APP_TITLE', 'version':{'title':'Versão:0.0.1', 'number':'0.0.1'}}
        button_add = structure2Extjs.Button('add', structure2Extjs.Configuration_Initial.BUTON_ADD_LABEL, structure2Extjs.Configuration_Initial.BUTTON_ADD_PATH_IMAGE, structure2Extjs.Configuration_Initial.BUTON_ADD_TOOLTIP)
        button_del = structure2Extjs.Button('del', structure2Extjs.Configuration_Initial.BUTON_DEL_LABEL, structure2Extjs.Configuration_Initial.BUTTON_DEL_PATH_IMAGE, structure2Extjs.Configuration_Initial.BUTON_DEL_TOOLTIP)
        button_save = structure2Extjs.Button('save', structure2Extjs.Configuration_Initial.BUTON_SAVE_LABEL, structure2Extjs.Configuration_Initial.BUTTON_SAVE_PATH_IMAGE, structure2Extjs.Configuration_Initial.BUTON_SAVE_TOOLTIP)
        button_cancel = structure2Extjs.Button('cancel', structure2Extjs.Configuration_Initial.BUTON_CANCEL_LABEL, structure2Extjs.Configuration_Initial.BUTTON_CANCEL_PATH_IMAGE, structure2Extjs.Configuration_Initial.BUTON_CANCEL_TOOLTIP)
        button_report = structure2Extjs.Button('report', structure2Extjs.Configuration_Initial.BUTTON_REPORT_LABEL, structure2Extjs.Configuration_Initial.BUTTON_REPORT_PATH_IMAGE, structure2Extjs.Configuration_Initial.BUTTON_REPORT_TOOLTIP)
        buttons = {button_add.action :button_add.get_configurations(),
                button_del.action :button_del.get_configurations(),
                button_save.action :button_save.get_configurations(),
                button_cancel.action :button_cancel.get_configurations(),
                button_report.action :button_report.get_configurations()}
        action_delete = structure2Extjs.Action(structure2Extjs.Configuration_Initial.ACTION_DELETE, structure2Extjs.Configuration_Initial.ACTION_DELETE_TITLE, structure2Extjs.Configuration_Initial.ACTION_DELETE_MSG)
        actions = {action_delete.action:action_delete.get_configurations()}
        ajax = structure2Extjs.Ajax(structure2Extjs.Configuration_Initial.AJAX_FAILURE, structure2Extjs.Configuration_Initial.AJAX_FAILURE_TITLE, structure2Extjs.Configuration_Initial.AJAX_FAILURE_MSG)
        ajax = {ajax.type_msg:ajax.get_configurations()}
        item_menu1 = structure2Extjs.Item_Menu('Menu1', 'click_menu', 'Tela de Listagem1', '/get_columns/link1/', 'url_load_grid', '/delete/father/', 'Tela de Entrada1', '/get_fields/link1/', '/save_form/form1/')
        item_menu2 = structure2Extjs.Item_Menu('Menu2', 'click_menu', 'Tela de Listagem2', '/get_columns/link2/', 'url_load_grid', '/delete/father/', 'Tela de Entrada2', '/get_fields/link2/', '/save_form/form2/')
        menu = structure2Extjs.Menu('Arquivo', [item_menu1, item_menu2])
        menu_exit = structure2Extjs.Menu_Exit(structure2Extjs.Configuration_Initial.MENU_EXIT_TITLE, structure2Extjs.Configuration_Initial.MENU_EXIT_ACTION, structure2Extjs.Configuration_Initial.MENU_EXIT_URL)
        menus = []
        menus.append(menu.menu2dict())
        menus.append('->')
        menus.append('-')
        menus.append(menu_exit.item_menu_exit2dict())
        configuration_initial_expected['button'] = buttons
        configuration_initial_expected['actions'] = actions
        configuration_initial_expected['ajax'] = ajax
        configuration_initial_expected['menu'] = menus
        configurations_initial = structure2Extjs.Configuration_Initial([menu])
        self.assertDictEqual(configuration_initial_expected, configurations_initial.configuration_Initial2dict())


class ListenerConfigTest(TestCase):
    def testAddEvent(self):
        testObject = structure2Extjs.ListenersConfig()
        testObject.addListenerEvent('change', 'functionName', value=1)
        self.assertTrue(hasattr(testObject, 'change'))

    def testUpdateListenerArgumentsExistentEvent(self):
        testObject = structure2Extjs.ListenersConfig()
        expectedAnswer = 2
        testObject.addListenerEvent('change', 'functionName', value=1)
        testObject.updateEventArguments('change', value_2=1)
        self.assertEqual(expectedAnswer, len(testObject.change[1]))

    def testUpdateListenerArgumentsNonExistentEvent(self):
        testObject = structure2Extjs.ListenersConfig()
        expectedAnswer = 2
        self.assertRaises(AttributeError, testObject.updateEventArguments, 'change', value=1)

    def testGetListenerConfigAsDict(self):
        testObject = structure2Extjs.ListenersConfig()
        testObject.addListenerEvent('change', 'functionName', value_1=1, value_2='test')
        expectedAnswer = {'listeners':{'change':'functionName', 'changeOptions':{'value_1':1, 'value_2':'test'}}}
        self.assertDictEqual(expectedAnswer, testObject.as_dict())


class FunctionJavaScriptTest(TestCase):
    def test_function_any_parameters(self):
        function_javascript = structure2Extjs.FunctionJavaScript(function_name='function_name')
        expectedAnswer = {'function_name':'function_name()'}
        self.assertDictEqual(expectedAnswer, function_javascript.as_dict())

    def test_function_with_parameters(self):
        function_javascript = structure2Extjs.FunctionJavaScript(function_name='function_name', function_parameters={1:'Um', 2:'Dois'})
        expectedAnswer = {'function_name':'function_name(Um,Dois)'}
        self.assertDictEqual(expectedAnswer, function_javascript.as_dict())


class TestDeleteRegister(TestCase):
    PROTECT_ERROR_MSG = u'O registro não pode ser removido, pois ele é referencia direta para [%s] de model on delete, remova primeiro esses registros.'
    
    def setUp(self):
        self.c = Client()
        self.c.get('/appExtjs/')
        self.base_delete_url = '/appExtjs/delete/appExtjs/'

    def testDeleteOnProtected(self):
        father = models.Father.objects.create(name='papai smurf')
        registerProtected = models.ModelOnDelete.objects.create(name='Name1', foreignKeyFieldProtect=father)
        response = self.c.post(self.base_delete_url + 'Father/%s/' %father.pk)
        responseExpected = {"msg": self.PROTECT_ERROR_MSG % registerProtected, 'success':False, 'title':u'Exclusão'}
        self.assertDictEqual(simplejson.loads(response.content), responseExpected)

    def testDeleteOnProtectedTwoObjects(self):
        father = models.Father.objects.create(name='papai smurf')
        registerProtected1 = models.ModelOnDelete.objects.create(name='Name1', foreignKeyFieldProtect=father)
        registerProtected2 = models.ModelOnDelete.objects.create(name='Name2', foreignKeyFieldProtect=father)
        response = self.c.post(self.base_delete_url + 'Father/%s/' %father.pk)
        parametersMsgc = unicode(registerProtected1) + ', ' + unicode(registerProtected2)
        msg = self.PROTECT_ERROR_MSG % parametersMsgc
        responseExpected = {"msg": msg, 'success':False, 'title':u'Exclusão'}
        self.assertDictEqual(simplejson.loads(response.content), responseExpected)

    def testDeleteOnCascade(self):
        father = models.Father.objects.create(name='papai smurf')
        registerProtected = models.ModelOnDelete.objects.create(name='Name1', foreignKeyFieldCascade=father)        
        response = self.c.post(self.base_delete_url + 'Father/%s/' %father.pk)
        responseExpected = {"msg": u'Registro removido com sucesso.', 'success':True, 'title':u'Exclusão'}
        self.assertDictEqual(simplejson.loads(response.content), responseExpected)
        self.assertEqual(0, models.ModelOnDelete.objects.filter(name='Name1').count())

    def testDeleteOnSetNull(self):
        father = models.Father.objects.create(name='papai smurf')
        registerProtected = models.ModelOnDelete.objects.create(name='Name1', foreignKeyFieldSetNull=father)
        response = self.c.post(self.base_delete_url + 'Father/%s/' %father.pk)
        responseExpected = {"msg": u'Registro removido com sucesso.', 'success':True, 'title':u'Exclusão'}
        self.assertDictEqual(simplejson.loads(response.content), responseExpected)
        registerProtected = models.ModelOnDelete.objects.get(name='Name1')
        foreignKeyFieldSetNullExpected = None
        self.assertEqual(foreignKeyFieldSetNullExpected, registerProtected.foreignKeyFieldSetNull)

class TestLoadGrid(TestCase):
    def setUp(self):
        self.fatherA = models.Father.objects.create(name='a')
        self.fatherB = models.Father.objects.create(name='b')
        self.base_load_grid_url = '/gridExtjs/load_model_in_grid_extjs/appExtjs/'

    def testGetAllRegisterNotSorted(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/')
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize(models.Father.objects.all())
        self.assertEqual(expect_answer, response.content)

    def testGetAllRegisterOrderByNameAsc(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'sort': '[{"property":"name", "direction":"ASC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherA, self.fatherB])
        self.assertEqual(expect_answer, response.content)

    def testGetAllRegisterOrderByNameDesc(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'sort': '[{"property":"name", "direction":"DESC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherB, self.fatherA])
        self.assertEqual(expect_answer, response.content)

    def testGetAllRegisterOrderByField1DescAndField2Asc(self):
        grandFatherA = models.GrandFather.objects.create(name='a', age=2)
        grandFatherB = models.GrandFather.objects.create(name='a', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'sort': '[{"property":"name", "direction":"DESC"}, {"property":"age", "direction":"ASC"}]'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB, grandFatherA])
        self.assertEqual(expect_answer, response.content)

    def testFilterByString(self):
        c = Client()
        response = c.get(self.base_load_grid_url + 'Father/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'A', 'filter[0][field]': 'name'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([self.fatherA])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldStringAndOneFieldInt(self):
        grandFatherA = models.GrandFather.objects.create(name='b', age=10)
        grandFatherB = models.GrandFather.objects.create(name='b', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'B', 'filter[0][field]': 'name',
                                                          'filter[1][data][type]': 'numeric', 'filter[1][data][value]': '1', 'filter[1][field]': 'age', 'filter[1][data][comparison]': 'eq'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldIntGreaterThan(self):
        grandFatherA = models.GrandFather.objects.create(name='b', age=10)
        grandFatherB = models.GrandFather.objects.create(name='a', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'numeric', 'filter[0][data][value]': '1', 'filter[0][field]': 'age', 'filter[0][data][comparison]': 'gt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherA])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldIntLessThan(self):
        grandFatherA = models.GrandFather.objects.create(name='b', age=10)
        grandFatherB = models.GrandFather.objects.create(name='a', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'filter[0][data][type]': 'numeric', 'filter[0][data][value]': '10', 'filter[0][field]': 'age', 'filter[0][data][comparison]': 'lt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([grandFatherB])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldDateEqual(self):
        datasA = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '20/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'eq'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasA])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldDateGreaterThan(self):
        datasA = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '20/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'gt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasB])
        self.assertEqual(expect_answer, response.content)

    def testFilterWithOneFieldDateLessThan(self):
        datasA = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/', {'filter[0][data][type]': 'date', 'filter[0][data][value]': '21/11/2012', 'filter[0][field]': 'dataNascimento', 'filter[0][data][comparison]': 'lt'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasA])
        self.assertEqual(expect_answer, response.content)

    def testGetPage1(self):
        grandFatherA = models.GrandFather.objects.create(name='b', age=10)
        grandFatherB = models.GrandFather.objects.create(name='a', age=1)
        grandFatherC = models.GrandFather.objects.create(name='c', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'limit': '2', 'start': '0', 'page': '1'})
        expect_answer = simplejson.dumps({'total': '3', "register": [
                                                               {"pk": grandFatherA.pk, "age": grandFatherA.age, "name": grandFatherA.name},
                                                               {"pk": grandFatherB.pk, "age": grandFatherB.age, "name": grandFatherB.name},
                                                               ]})
        self.assertEqual(expect_answer, response.content)

    def testGetPage2(self):
        grandFatherA = models.GrandFather.objects.create(name='b', age=10)
        grandFatherB = models.GrandFather.objects.create(name='a', age=1)
        grandFatherC = models.GrandFather.objects.create(name='c', age=1)
        c = Client()
        response = c.get(self.base_load_grid_url + 'GrandFather/', {'limit': '2', 'start': '2', 'page': '2'})
        expect_answer = simplejson.dumps({'total': '3', "register": [{"pk": grandFatherC.pk, "age": grandFatherC.age, "name": grandFatherC.name}]})
        self.assertEqual(expect_answer, response.content)

    def testFilterWithForeign(self):
        forTestsForeignKey1 = models.ForTestsForeignKey.objects.create(name='ForTestsForeignKey1', foreignKeyField=self.fatherA)
        forTestsForeignKey2 = models.ForTestsForeignKey.objects.create(name='ForTestsForeignKey2', foreignKeyField=self.fatherB)
        c = Client()
        response = c.get(self.base_load_grid_url + 'ForTestsForeignKey/', {'filter[0][data][type]': 'string', 'filter[0][data][value]': 'a', 'filter[0][field]': 'foreignKeyField__name'})
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([forTestsForeignKey1])
        self.assertEqual(expect_answer, response.content)

    def testOrderWithParametersOfModel(self):
        datasA = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 20))
        datasB = models.Datas.objects.create(dataNascimento=datetime.date(2012, 11, 21))
        c = Client()
        response = c.get(self.base_load_grid_url + 'Datas/')
        expect_answer = json2Extjs.ExtJSONSerialiser().serialize([datasB, datasA])
        self.assertEqual(expect_answer, response.content)
