from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^render_form/(?P<form_name>.*)/$', 'formExtjs.views.render_form'),
)