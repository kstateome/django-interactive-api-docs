from django.shortcuts import render
from api_docs.models import *

def home(request):
    context = {'apis':APIDoc.objects.all()}
    return render(request, 'api_docs/apis.html', context)
    
def build_js(request):
    context = {'apis': APIDoc.objects.all()}
    return render(request, 'api_docs/docs.js', context)

def soap_call(request, api_method_id=None):
    """
    Makes the SOAP based api call, and returns the dump of xml.  This is called via ajax
    by the browser to appear that the call was async.
    """
    return render(request, "api_docs/apis.html", context)