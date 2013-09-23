  # -*- encoding: utf-8 -*-
from django.utils import simplejson
from django.core.context_processors import csrf
from django.db.models import ProtectedError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models.loading import get_model

import formExtjs
from gridExtjs.views import Collumns2GridExtjs
import structure2Extjs

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = object.__new__(cls, *args, **kwargs)
        return cls._inst

class Configuration(Singleton):
    def __init__(self, configuration_initial=None):
        if configuration_initial:
            self.configuration_initial = configuration_initial

def main(request, configuration_initial=structure2Extjs.Configuration_Initial()):
    configuration = Configuration(configuration_initial)
    return render_to_response("index.html", {'app_title':configuration.configuration_initial.APP_TITLE}, context_instance=RequestContext(request))

def get_configurations_initial(request):
    configuration = Configuration()
    configuration_initial_dict = configuration.configuration_initial.configuration_Initial2dict()
    return HttpResponse(simplejson.dumps(configuration_initial_dict), mimetype='application/json')

def get_columns(request, app_name, model_name, **kwargs):
    model = get_model(app_name,model_name)
    permissions = kwargs.pop('permissions', {})
    collumns2GridExtjs = Collumns2GridExtjs(**kwargs)
    fields = simplejson.loads(collumns2GridExtjs.output_extjs(model))
    data = {'columns':fields, 'permissions':permissions}
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def get_fields(request, form, id):
    instance = None
    if id:
        if hasattr(form, "_meta"):
            instance = form._meta.model.objects.get(pk=id)
        else:
            instance = form.fk.rel.to.objects.get(pk=id)
    form = form(instance=instance)
    fields = formExtjs.views.fields_form2extjs(form, unicode(csrf(request)['csrf_token']))
    fields = simplejson.dumps(fields)
    return HttpResponse(fields, mimetype='application/json')

def load_combobox(request, model):
    data = model_to_combobox(model)
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def model_to_combobox(model):
    models = model.objects.all()
    result = []
    for model in models:
        result.append({'key': model.id, 'value': unicode(model)})
    return result

def save_form(request, form):
    data = {'success':True}
    if request.method == "POST":
        try:
            if hasattr(form, '_meta'):
                object = form._meta.model.objects.get(pk=request.POST['pk'])
            else:
                object = form.fk.rel.to.objects.get(pk=request.POST['pk'])
            form = form(request.POST, request.FILES, instance=object)
        except:
            form = form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            data = {'success':False, 'errors':form.errors}
    return HttpResponse(simplejson.dumps(data), mimetype='text/html')

def delete(request, app_name, model_name, id):
    model = get_model(app_name,model_name)
    object = model.objects.get(pk=id)
    data = {'success': True}
    configuration = Configuration()
    data['title'] = configuration.configuration_initial.DELETE_SUCESS_TITLE
    data['msg'] = configuration.configuration_initial.DELETE_SUCESS_MSG
    if request.method == "POST":
        try:
            object.delete()
        except ProtectedError, error:
            data['success'] = False
            data['msg'] = getMsgDeleteProtectedError(error)
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def getMsgDeleteProtectedError(error):
    objectsProtected = list(error[1])
    joinVerboseOfTheObjectsProtected = lambda acc, objectProtected: acc + ', ' + unicode(objectProtected)
    parameterObjects = reduce(joinVerboseOfTheObjectsProtected, objectsProtected[1:], unicode(objectsProtected[0]))
    parameterModel = objectsProtected[0]._meta.verbose_name
    configuration = Configuration()
    return configuration.configuration_initial.DELETE_EXCEPT_PROTECTED_ERROR_MSG % (parameterObjects, parameterModel)