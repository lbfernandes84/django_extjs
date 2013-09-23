# -*- encoding: utf-8 -*-
import sys
sys.path.append('..')
import os
import tempfile
from django.test import TestCase
from django import forms

from .. import views, models, forms_app

class FieldTest(TestCase):
    def test_boolean_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'checkboxfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Boolean field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["boolean_field"])
        self.assertDictEqual(expect, result)

    def test_boolean_field1_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'checkboxfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'BFTeste'
        expect['checked'] = True
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["boolean_field1"])
        self.assertDictEqual(expect, result)

    def test_char_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Char field'
        expect['maxLength'] = 10
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["char_field"])
        self.assertDictEqual(expect, result)

    def test_choice_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'choice_field'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Choice field'
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': 1, 'value': u'Um'}, {'key': 2, 'value': u'Dois'}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["choice_field"], name_field='choice_field')
        self.assertDictEqual(expect, result)

    def test_typed_choice_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'typed_choice_field'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Typed choice field'
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': 1, 'value': u'Um'}, {'key': 2, 'value': u'Dois'}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["typed_choice_field"], name_field='typed_choice_field')
        self.assertDictEqual(expect, result)

    def test_decimal_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'numberfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Decimal field'
        expect['maxLength'] = 7
        expect['enforceMaxLength'] = True
        expect['decimalPrecision'] = 3
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["decimal_field"])
        self.assertDictEqual(expect, result)

    def test_email_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['vtype'] = 'email'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Email field'
        expect['maxLength'] = 75
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["email_field"])
        self.assertDictEqual(expect, result)

    def test_float_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'numberfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Float field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["float_field"])
        self.assertDictEqual(expect, result)

    def test_integer_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'numberfield'
        expect['allowDecimals'] = False
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Integer field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["integer_field"])
        self.assertDictEqual(expect, result)

    def test_url_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['vtype'] = 'url'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Url field'
        expect['maxLength'] = 200
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["url_field"])
        self.assertDictEqual(expect, result)

    def test_ip_address_field_2_Extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['vtype'] = 'iPAddress'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Ip address field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["ip_address_field"])
        self.assertDictEqual(expect, result)

    def test_generic_ip_address_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Generic ip address field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["generic_ip_address_field"])
        self.assertDictEqual(expect, result)

    def test_date_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'datefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Date field'
        expect['format'] = 'd/m/Y'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["date_field"])
        self.assertDictEqual(expect, result)

    def test_time_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'timefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Time field'
        expect['format'] = 'H:i'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["time_field"])
        self.assertDictEqual(expect, result)

    def test_date_time_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'datefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Date time field'
        expect['format'] = 'd/m/Y H:i:s'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["date_time_field"])
        self.assertDictEqual(expect, result)

    def test_slug_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Slug field'
        expect['maxLength'] = 50
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["slug_field"])
        self.assertDictEqual(expect, result)

    def test_file_path_field_2_extjs(self):
        dir_path_temp = tempfile.mkdtemp()
        file_temp = tempfile.TemporaryFile(dir=dir_path_temp)
        class Form2Test(forms.Form):
            file_path_field = forms.FilePathField(path=dir_path_temp)
        form = Form2Test()
        expect = {}
        expect['name'] = 'file_path_field'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'File path field'
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': file_temp.name, 'value': os.path.split(file_temp.name)[1]}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields['file_path_field'], name_field='file_path_field')
        self.assertDictEqual(expect, result)

    def test_multiple_choice_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'multiple_choice_field'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Multiple choice field'
        expect['multiSelect'] = True
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': 1, 'value': 'Um'}, {'key': 2, 'value': 'Dois'}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields['multiple_choice_field'], name_field='multiple_choice_field')
        self.assertDictEqual(expect, result)

    def test_typed_multiple_choice_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'typed_multiple_choice_field'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Typed multiple choice field'
        expect['multiSelect'] = True
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': 1, 'value': 'Um'}, {'key': 2, 'value': 'Dois'}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields['typed_multiple_choice_field'], name_field='typed_multiple_choice_field')
        self.assertDictEqual(expect, result)

    def test_null_boolean_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = ''
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Null boolean field'
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'key': u'1', 'value': u'Desconhecido'},
                                                                {'key': u'2', 'value': u'Sim'},
                                                                {'key': u'3', 'value': u'Não'}]}
        expect['msgTarget'] = 'under'
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["null_boolean_field"])
        self.assertDictEqual(expect, result)

    def test_regex_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'regex_field'
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Regex field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["regex_field"], name_field='regex_field')
        self.assertDictEqual(expect, result)

    def test_file_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'file_field'
        expect['xtype'] = 'filefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'File field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        expect['value'] = ''
        result = views.field2extjs(form.fields["file_field"], name_field='file_field')
        self.assertDictEqual(expect, result)

    def test_image_field_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'image_field'
        expect['xtype'] = 'filefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Image field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        expect['value'] = ''
        result = views.field2extjs(form.fields["image_field"], name_field='image_field')
        self.assertDictEqual(expect, result)

    def test_char_field_with_password_widget_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'password_field'
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Password field'
        expect['inputType'] = 'password'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["password_field"], name_field='password_field')
        self.assertDictEqual(expect, result)

    def test_char_field_with_hidden_widget_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'hidden_field'
        expect['xtype'] = 'textfield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Hidden field'
        expect['hidden'] = True
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["hidden_field"], name_field='hidden_field')
        self.assertDictEqual(expect, result)

    def test_field_with_widget_file_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'file_widget_field'
        expect['xtype'] = 'filefield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'File widget field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        expect['value'] = ''
        result = views.field2extjs(form.fields["file_widget_field"], name_field='file_widget_field')
        self.assertDictEqual(expect, result)

    def test_char_field_with_text_area_widget_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'text_area_field'
        expect['xtype'] = 'textareafield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Text area field'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["text_area_field"], name_field='text_area_field')
        self.assertDictEqual(expect, result)

    def test_choice_field_with_radio_widget_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'radio_field'
        expect['xtype'] = 'fieldcontainer'
        expect['defaultType'] = 'radiofield'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Radio field'
        expect['items'] = [{'boxLabel': u'Um', 'inputValue': 1}, {'boxLabel': u'Dois', 'inputValue': 2}]
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["radio_field"], name_field='radio_field')
        self.assertDictEqual(expect, result)

    def test_multiple_choice_field_with_checkbox_select_multiple_widget_2_extjs(self):
        form = forms_app.FormTesteTT()
        expect = {}
        expect['name'] = 'checkbox_select_multiple_field'
        expect['xtype'] = 'fieldcontainer'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Checkbox select multiple field'
        expect['multiSelect'] = True
        expect['defaultType'] = 'checkboxfield'
        expect['items'] = [{'boxLabel': u'Um', 'inputValue': 1}, {'boxLabel': u'Dois', 'inputValue': 2}]
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields['checkbox_select_multiple_field'], name_field='checkbox_select_multiple_field')
        self.assertDictEqual(expect, result)

class testModelForm(TestCase):
    def test_model_form_unbound(self):
        form = forms_app.ChildForm()
        expect = [{'xtype': 'hiddenfield', 'value': None, 'name': 'pk'},
            {'xtype': 'textfield', 'fieldLabel': u'Name', 'allowBlank': False, 'maxLength': 10, 'name':'name', 'msgTarget':'under', 'anchor':'100%'},
            {'displayField': 'value', 'fieldLabel': u'Father', 'allowBlank': False, 
            'valueField': 'key', 'store': {'fields': ['key', 'value'], 'data': [{'value': u'---------', 'key': u''}, ]}, 
            'xtype': 'combobox', 'name':'father', 'msgTarget':'under', 'anchor':'100%'}]
        result = views.fields_form2extjs(form)
        self.assertListEqual(expect, result)

    def test_model_form_bound(self):
        father = models.Father.objects.create(name='father1')
        child1 = models.Child.objects.create(name='child1', father=father)
        form = forms_app.ChildForm({'name':'child1', 'father':father.pk})
        expect = [{'xtype': 'hiddenfield', 'value': None, 'name': 'pk'},
            {'xtype': 'textfield', 'fieldLabel': u'Name', 'allowBlank': False, 'value': u'child1', 'maxLength': 10, 'name':'name', 'msgTarget':'under', 'anchor':'100%'},
            {'displayField': 'value', 'fieldLabel': u'Father', 'allowBlank': False, 'value': 1, 
            'valueField': 'key', 'store': {'fields': ['key', 'value'], 'data': [{'value': u'---------', 'key': u''}, 
            {'value': u'Father object', 'key': 1}]}, 'xtype': 'combobox', 'name':'father', 'msgTarget':'under', 'anchor':'100%'}]
        result = views.fields_form2extjs(form)
        self.assertListEqual(expect, result)

    def test_modelform_with_instance(self):
        father = models.Father.objects.create(name='father1')
        child1 = models.Child.objects.create(name='child1', father=father)
        form = forms_app.ChildForm(instance=child1)
        expect = [{'xtype': 'hiddenfield', 'value': child1.pk, 'name': 'pk'},
            {'xtype': 'textfield', 'fieldLabel': u'Name', 'allowBlank': False, 'value': u'child1', 'maxLength': 10, 'name':'name', 'msgTarget':'under', 'anchor':'100%'},
            {'displayField': 'value', 'fieldLabel': u'Father', 'allowBlank': False, 'value': father.pk, 
            'valueField': 'key', 'store': {'fields': ['key', 'value'], 'data': [{'value': u'---------', 'key': u''}, 
            {'value': u'Father object', 'key': 1}]}, 'xtype': 'combobox', 'name':'father', 'msgTarget':'under', 'anchor':'100%'}]
        result = views.fields_form2extjs(form)
        self.assertListEqual(expect, result)

    def test_char_field_with_choices(self):
        form = forms_app.CharFieldWithChoicesForm()
        expect = {}
        expect['name'] = 'name'
        expect['xtype'] = 'combobox'
        expect['allowBlank'] = False
        expect['fieldLabel'] = 'Name'
        expect['store'] = {'fields': ['key', 'value'], 'data': [{'value': u'---------', 'key': u''}, 
                                                                {'key': 1, 'value': u'Um'}, 
                                                                {'key': 2, 'value': u'Dois'}]}
        expect['displayField'] = 'value'
        expect['valueField'] = 'key'
        expect['msgTarget'] = 'under'
        expect['anchor'] = '100%'
        result = views.field2extjs(form.fields["name"], name_field='name')
        self.assertDictEqual(expect, result)

    def test_alter_widget(self):
        poll = models.Poll.objects.create(question='what is?')
        choice1 = models.Choice.objects.create(poll=poll, choice='choice1')
        choice2 = models.Choice.objects.create(poll=poll, choice='choice2')
        form = forms_app.ChoiceForm({'poll':poll.pk})
        expect = [{'xtype': 'hiddenfield', 'value': None, 'name': 'pk'},
            {'displayField': 'value', 'fieldLabel': u'Poll', 'allowBlank': False, 'value': 1, 
            'valueField': 'key', 'store': {'fields': ['key', 'value'], 'data': [{'value': u'---------', 'key': u''}, 
            {'value': u'Poll object', 'key': 1}]}, 'xtype': 'combobox', 'name': 'poll', 'msgTarget':'under', 'anchor':'100%'},
            {'displayField': 'value', 'fieldLabel': u'Choice', 'allowBlank': False, 
            'valueField': 'key', 'maxLength': 200, 'store': {'fields': ['key', 'value'], 
            'data': [{'value': u'Choice object', 'key': 1}, 
                    {'value': u'Choice object', 'key': 2}]}, 
            'xtype': 'combobox', 'name': 'choice', 'msgTarget':'under', 'anchor':'100%'}]
        result = views.fields_form2extjs(form)
        self.assertListEqual(expect, result)
