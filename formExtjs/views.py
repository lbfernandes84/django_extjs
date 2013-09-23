from django import forms
from django.utils.encoding import force_unicode, force_text
from django.db import models

def fields_form2extjs(form, csrf_token='', isLoginForm=False):
    fields_extjs = []
    try:
        if csrf_token:
            fields_extjs.append({'xtype': 'hiddenfield', 'name': 'csrfmiddlewaretoken', 'value': force_text(csrf_token)})
        try:
            pk = form.instance.pk
        except:
            pk = None
        fields_extjs.append({'xtype': 'hiddenfield', 'name': 'pk', 'value': pk})
        for name, field in form.fields.items():
            value_field = form.data.get(name,'')
            if not value_field:
                try:
                    instance = getattr(form,'instance')
                    value_field = getattr(instance, name)
                    if isinstance(value_field, models.Model):
                        value_field = str(value_field)
                except:
                    pass
            fields_extjs.append(field2extjs(field=field, name_field=name,value_field=value_field))
    except:
        pass
    return fields_extjs

DATE_FORMAT = {'%d/%m/%Y': 'd/m/Y'}
TIME_FORMAT = {'%H:%M':'H:i'}
DATE_TIME_FORMAT_FIELD = {'%d/%m/%Y %H:%M:%S':'d/m/Y H:i:s'}
def field2extjs(field, name_field='', value_field='', date_format=DATE_FORMAT, time_format=TIME_FORMAT, date_time_format=DATE_TIME_FORMAT_FIELD):
    result = {}
    result['name'] = name_field
    result['fieldLabel'] = field.label or forms.forms.pretty_name(name_field)
    result['allowBlank'] = not field.required
    result['msgTarget'] = 'under'
    result['anchor'] = '100%'
    if field.initial and not value_field:
            value_field = field.initial
    if value_field:
        result['value'] = value_field
    if hasattr(field, 'min_value') and field.min_value:
        result['minValue'] = field.min_value
    if hasattr(field, 'max_value') and field.max_value:
        result['maxValue'] = field.max_value
    if hasattr(field, 'min_length') and field.min_length:
        result['minLength'] = field.min_length
    if hasattr(field, 'max_length') and field.max_length:
        result['maxLength'] = field.max_length
    if hasattr(field.widget, 'allow_multiple_selected') and field.widget.allow_multiple_selected:
        result['multiSelect'] = field.widget.allow_multiple_selected
    if isinstance(field, forms.fields.NullBooleanField):
        result['xtype'] = 'combobox'
        result['allowBlank'] = False
        data = []
        for item in field.widget.choices:
            data.append({'key': item[0], 'value': force_unicode(item[1])})
        result['store'] = {'fields': ['key', 'value'], 'data': data}
        result['displayField'] = 'value'
        result['valueField'] = 'key'
    elif isinstance(field.widget, forms.widgets.CheckboxInput):
        result['xtype'] = 'checkboxfield'
        result['allowBlank'] = field.required
        if field.initial:
            result['checked'] = result.pop('value')
    elif isinstance(field.widget, forms.widgets.Textarea):
        result['xtype'] = 'textareafield'
    elif isinstance(field.widget, forms.widgets.PasswordInput):
        result['xtype'] = 'textfield'
        result['inputType'] = 'password'
    elif isinstance(field.widget, forms.widgets.HiddenInput):
        result['xtype'] = 'textfield'
        result['hidden'] = True
    elif isinstance(field.widget, forms.widgets.Select):
        choices = getattr(field, 'choices', None)
        choices = choices or getattr(field.widget, 'choices', None)
        if isinstance(field.widget, (forms.widgets.RadioSelect, forms.widgets.CheckboxSelectMultiple)):
            result['xtype'] = 'fieldcontainer'
            data = []
            for item in choices:
                data.append({'inputValue': item[0], 'boxLabel': item[1]})
            result['items'] = data
            if isinstance(field.widget, forms.widgets.RadioSelect):
                result['defaultType'] = 'radiofield'
            else:
                result['defaultType'] = 'checkboxfield'
        else:
            result['xtype'] = 'combobox'
            data = []
            for item in choices:
                data.append({'key': item[0], 'value': item[1]})
                if item[1] == value_field:
                    result['value'] = item[0]
            result['store'] = {'fields': ['key', 'value'], 'data': data}
            result['displayField'] = 'value'
            result['valueField'] = 'key'
    elif isinstance(field.widget, forms.widgets.DateInput):
        result['xtype'] = 'datefield'
        if field.widget.format in date_format:
            format_python = field.widget.format
            format_extjs = date_format[format_python]
        else:
            format_python = '%d/%m/%Y'
            format_extjs = 'd/m/Y'
            field.widget.format = format_python
        if value_field:
            result['value'] = value_field.strftime(format_python)
        result['format'] = format_extjs
    elif isinstance(field.widget, forms.widgets.TimeInput):
        result['xtype'] = 'timefield'
        if field.widget.format in time_format:
            format_python = field.widget.format
            format_extjs = time_format[format_python]
        else:
            format_python = '%H:%M'
            format_extjs = 'H:i'
            field.widget.format = format_python
        if value_field:
            result['value'] = value_field.strftime(format_python)
        result['format'] = format_extjs
    elif isinstance(field.widget, forms.widgets.DateTimeInput):
        result['xtype'] = 'datefield'
        if field.widget.format in date_time_format:
            format_python = field.widget.format
            format_extjs = date_time_format[format_python]
        else:
            format_python = '%d/%m/%Y %H:%M:%S'
            format_extjs = 'd/m/Y H:i:s'
            field.widget.format = format_python
        if value_field:
            result['value'] = value_field.strftime(format_python)
        result['format'] = format_extjs
    elif isinstance(field.widget, forms.widgets.TextInput):
        result['xtype'] = 'textfield'
        if isinstance(field, forms.EmailField):
            result['vtype'] = 'email'
        elif isinstance(field, forms.URLField):
            result['vtype'] = 'url'
        elif isinstance(field, forms.IPAddressField):
            result['vtype'] = 'iPAddress'
        elif isinstance(field, forms.FloatField):
            result['xtype'] = 'numberfield'
        elif isinstance(field, forms.DecimalField):
            result['xtype'] = 'numberfield'
            result['maxLength'] = field.max_digits + 1 #O +1 representa o separador decimal, pois ele conta no extjs
            result['enforceMaxLength'] = True
            result['decimalPrecision'] = field.decimal_places
        elif isinstance(field, forms.IntegerField):
            result['xtype'] = 'numberfield'
            result['allowDecimals'] = False
    elif isinstance(field.widget, (forms.widgets.ClearableFileInput, forms.widgets.FileInput)):
        result['xtype'] = 'filefield'
        result['value'] = force_text(value_field)
    return result
