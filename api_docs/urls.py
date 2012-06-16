from django.conf.urls.defaults import patterns, include, url
from api_docs.views import home, build_js, soap_call

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^js/docs.js', build_js, name="build_js"),
    url(r'^ajax/soap/$', soap_call, name="soap_api_call"),
)
