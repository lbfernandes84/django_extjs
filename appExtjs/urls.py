from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'appExtjs.views.main'),
    url(r'^get_columns/(?P<app_name>.*)/(?P<model_name>.*)/$', 'appExtjs.views.get_columns'),
    url(r'^get_fields/(?P<form_name>.*)/(?P<id>.*)$', 'appExtjs.views.get_fields'),
    url(r'^save_form/(?P<form_name>.*)/$', 'appExtjs.views.save_form'),
    url(r'^delete/(?P<app_name>.*)/(?P<model_name>.*)/(?P<id>.*)/$', 'appExtjs.views.delete'),
    url(r'^get_configurations_initial/$', 'appExtjs.views.get_configurations_initial'),
)