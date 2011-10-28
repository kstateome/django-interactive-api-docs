from django.shortcuts import render_to_response
from api_docs.models import *
from django.template import RequestContext

def home(request):
    context = {'apis':APIDoc.objects.all()}
    return render_to_response('api_docs/apis.html', context, context_instance=RequestContext(request))
    
def build_js(request):
    context = {'apis': APIDoc.objects.all()}
    return render_to_response('api_docs/docs.js', context, context_instance=RequestContext(request))
