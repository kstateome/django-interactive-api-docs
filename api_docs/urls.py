from django.conf.urls.defaults import patterns, include, url
from api_docs.views import *
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^js/docs.js', build_js, name="build_js"),

    url(r'^admin/', include(admin.site.urls)),
)
