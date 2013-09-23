from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^load_model_in_grid_extjs/(?P<app_name>.*)/(?P<model_name>.*)/$', 'gridExtjs.views.load_grid'),
)