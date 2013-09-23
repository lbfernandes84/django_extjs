from appExtjs import forms as formsAppExtjs
from appExtjs import views

def get_fields(request, form_name, id):
    form = formsAppExtjs.__getattribute__(form_name)
    return views.get_fields(request, form, id)
