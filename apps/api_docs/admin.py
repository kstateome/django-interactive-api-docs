from django.contrib import admin
from api_docs.models import *
from django.contrib.contenttypes import generic
admin.site.register(APIDoc)
admin.site.register(APIObject)
    
class APIMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'api_object', 'api_url')
    save_on_top = True
    filter_vertical = ('parameter',)
    
    
admin.site.register(Parameter)
admin.site.register(APIMethod, APIMethodAdmin)