from django.shortcuts import render, get_object_or_404
from api_docs.models import *


def home(request):
    context = {'apis':APIDoc.objects.all()}
    return render(request, 'api_docs/apis.html', context)
    
def build_js(request):
    context = {'apis': APIDoc.objects.all()}
    return render(request, 'api_docs/docs.js', context)

def soap_call(request, soap_method_id):
    """
    Makes the SOAP based api call, and returns the dump of xml.  This is called via ajax
    by the browser to appear that the call was async.
    """
    # Grab all vars
    #for param in
    context = {}
    method = get_object_or_404(APIMethod, pk=soap_method_id)
    param_string = ""
    for param in method.parameter.all():
        param_string = param_string + "%s=%s," % (param.name, request.GET.get(param.name))
        print param_string
    return render(request, "api_docs/apis.html", context)