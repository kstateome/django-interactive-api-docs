from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^docs/', include('api_docs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './assets'}),
    url(r'^static_admin/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './admin_media'}),
)
