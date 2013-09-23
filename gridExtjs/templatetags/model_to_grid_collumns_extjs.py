from django.utils import simplejson
from django import template
from django.db.models.loading import get_model
register = template.Library()
from .. import views

@register.tag
def extract_fields_model_to_grid_extjs(parser, token):
    tag_name, app_name, model_name = token.split_contents()
    return Models2GridExtjsNode(app_name, model_name)
    
class Models2GridExtjsNode(template.Node):
    def __init__(self, app_name, model_name):
        self.app_name  = template.Variable(app_name)
        self.model_name  = template.Variable(model_name)
    
    def render(self, context):
        app_name = self.app_name.resolve(context)
        model_name = self.model_name.resolve(context)
        model = get_model(app_name,model_name)
        collumns2grid_extjs = views.Collumns2GridExtjs()
        return collumns2grid_extjs.output_extjs(model)