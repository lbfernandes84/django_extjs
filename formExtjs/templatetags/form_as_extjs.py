from django.utils import simplejson
from django import template
register = template.Library()
from .. import views

@register.tag
def do_form_as_extjs(parser, token):
    tag_name, form = token.split_contents()
    return Form2ExtjsNode(form)
    
class Form2ExtjsNode(template.Node):
    def __init__(self, form):
        self.form = template.Variable(form)
    
    def render(self, context):
        form = self.form.resolve(context)
        csrf_token = context.get('csrf_token','')
        form_in_extjs = views.fields_form2extjs(form, csrf_token)
        form_in_extjs = simplejson.dumps(form_in_extjs)
        return form_in_extjs