from django.db.models.fields.related import ForeignKey
from django.db.models import fields
from django.utils import simplejson
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models.loading import get_model
import datetime

import json2Extjs
import models

class CollumnGridExtjs(dict):
    '''
    Essa classe representa uma coluna do grid extjs
    '''
    def __init__(self, flex=1, data_index='', header='', hidden=False, filter_type='string'):
        self.flex = 1
        self.data_index = data_index
        self.header = header
        self.hidden = hidden
        self.update({'flex':self.flex, 'dataIndex':self.data_index, 'header':self.header})
        if self.hidden:
            self.update({'hidden':self.hidden})
        self.update({'filter':{'type':filter_type}})

class Collumns2GridExtjs(object):
    def __init__(self):
        self.__hidden_fields = []
        self.__extra_fields = {}
        self.__fields_order = []
        self.fields_extjs = []

    def output_extjs(self, model):
        fields = model._meta.fields
        self.get_options2extjs_from_model(model)
        self.__build_fields_columns_extjs(fields)
        self.__build_extra_fields_columns_extjs()
        self.__order_fields()
        return simplejson.dumps(self.fields_extjs)
        
    def get_options2extjs_from_model(self, model):
        self.__hidden_fields = []
        self.__extra_fields = {}
        self.__fields_order = []
        options_2_extjs = getattr(model, 'Options2GridExtjs', None)
        if options_2_extjs:
            self.__hidden_fields = getattr(options_2_extjs, 'name_fields_hidden', [])
            self.__extra_fields = getattr(options_2_extjs, 'extra_fields', {})
            self.__fields_order = getattr(options_2_extjs, 'name_fields_order', [])
        self.get_field_index = lambda field:self.__fields_order.index(field['dataIndex'])

    def __build_fields_columns_extjs(self, fields):
        for field in fields:
            collumn_extjs = self.get_collumn_extjs_for_django_model_field(field)
            self.fields_extjs.append(collumn_extjs)

    def __build_extra_fields_columns_extjs(self):
        LABEL_INDEX = 0
        for field, item in self.__extra_fields.items():
            collumn_grid_extjs = CollumnGridExtjs(data_index=field, header=item[LABEL_INDEX])
            self.fields_extjs.append(collumn_grid_extjs)

    def __order_fields(self):
        self.__complete_order()
        self.fields_extjs.sort(key=self.get_field_index)

    def __complete_order(self):
        for field in self.fields_extjs:
            try:
                index = self.get_field_index(field)
            except ValueError:
                self.__fields_order.append(field['dataIndex'])

    def get_collumn_extjs_for_django_model_field(self, field):
        data_index = field.name
        header = self.get_verbose_name_of_model_or_verbose_name_with_capitalize(field)
        hidden = False
        filter_type = self.get_filter_field_model_django_to_extjs(field)
        if field.name in self.__hidden_fields:
            hidden = True
        elif isinstance(field, fields.AutoField):
            header = field.verbose_name.capitalize()
            hidden = True
            data_index = 'pk'
            filter_type = 'numeric'
        elif self.field_is_foreignKey(field):
            hidden = True
        collumn_grid_extjs = CollumnGridExtjs(data_index=data_index, header=header, hidden=hidden, filter_type=filter_type)
        return collumn_grid_extjs

    def get_verbose_name_of_model_or_verbose_name_with_capitalize(self, field):
        header = field.verbose_name.capitalize()
        if header[1:] != field.verbose_name[1:]:
            header = field.verbose_name
        return header

    def field_is_foreignKey(self, field):
        return isinstance(field, ForeignKey)
        
    def get_filter_field_model_django_to_extjs(self, field):
        filter = 'string'
        if isinstance(field, (fields.DateField, fields.DateTimeField)):
            filter = 'date'
        elif isinstance(field, (fields.IntegerField, fields.BigIntegerField, fields.DecimalField, fields.FloatField, 
                                fields.PositiveIntegerField, fields.PositiveSmallIntegerField, fields.SmallIntegerField)):
            filter = 'numeric'
        elif isinstance(field, (fields.BooleanField, fields.NullBooleanField)):
            filter = 'boolean'
        return filter

def load_grid(request, app_name, model_name, queryset=None, filters={}, **kwargs):
    model = get_model(app_name, model_name)
    queryset = mountQuerySetWithParametersSortAndFilter(request, model, queryset, filters)
    pagination = getDatasPagination(request, queryset, **kwargs)
    return HttpResponse(pagination, mimetype="application/json")

def mountQuerySetWithParametersSortAndFilter(request, model, queryset=None, filters={}):
    sortParametersModels = model._meta.ordering
    if not queryset:
        sortParameters = getParametersSortExtjs2Django(request)
        sortParameters = sortParameters or sortParametersModels
        filterParameters = getFilterParametersExtjs2Django(request)
        filterParameters.update(filters)
        queryset = model.objects.all().order_by(*sortParameters).filter(**filterParameters)
    return queryset
    
def getParametersSortExtjs2Django(request):
    PARAMETERS_EXTJS_2_DJANGO = {'ASC': '', 'DESC': '-'}
    parameters = []
    sort = simplejson.loads(request.GET.get('sort', "[]"))
    for field in sort:
        parameters.append(PARAMETERS_EXTJS_2_DJANGO[field['direction']] + field['property'])
    return parameters
    
def getFilterParametersExtjs2Django(request):
    FILTERS_EXTJS_2_DJANGO = {'': '__iregex', 'eq': '__exact', 'gt': '__gt', 'lt': '__lt'}
    FILTER_FIELD_NAME = 'filter[%i][field]'
    FILTER_VALUE = 'filter[%i][data][value]'
    FILTER_TYPE = 'filter[%i][data][type]'
    FILTER_COMPARISON = 'filter[%i][data][comparison]'
    filters = {}
    index = 0
    while(FILTER_FIELD_NAME % index in request.GET):
        field = request.GET.get(FILTER_FIELD_NAME % index, '')
        comparisonMethod = request.GET.get(FILTER_COMPARISON % index, '')
        typeField = request.GET.get(FILTER_TYPE % index, '')
        value = request.GET.get(FILTER_VALUE % index, '')
        value = getValueInFormatDateOrValueOrigin(value, typeField)
        filters[field + FILTERS_EXTJS_2_DJANGO[comparisonMethod]] = value
        index += 1
    return filters

def getDatasPagination(request, queryset, **kwargs):
    page = request.GET.get('page', '')
    try:
        if page:
            limit = request.GET.get('limit')
            start = request.GET.get('start')
            p = Paginator(queryset, limit)
            pageSerialize = json2Extjs.ExtJSONSerialiser(**kwargs).serialize(p.page(page))
            data = '{"total": "%i", "register": %s}' % (p.count, pageSerialize)
        else:
            data = json2Extjs.ExtJSONSerialiser(**kwargs).serialize(queryset)
    except:
        data = '{"total": "0", "register":[]}'
    return data

def getValueInFormatDateOrValueOrigin(value, typeField):
    if typeField == 'date':
        try:
            value = datetime.datetime.strptime(value, json2Extjs.DATE_FORMAT_FIELD)
        except:
            value = None
    return value