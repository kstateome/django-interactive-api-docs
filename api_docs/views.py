from django.shortcuts import render, get_object_or_404
from api_docs.models import *
from django.http import HttpResponse

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

    # Bind suds client to the wsdl
    from suds.client import Client
    from api_docs import defaults
    proxy = getattr(settings, "SOAP_USE_PROXY", defaults.SOAP_USE_PROXY)
    if not proxy:
        soap_client = Client(method.api_url, username=getattr(settings, "SOAP_USERNAME", defaults.SOAP_USERNAME), password=getattr(settings, "SOAP_PASSWORD", defaults.SOAP_PASSWORD))
    else:
        soap_client = Client(method.api_url, proxy=getattr(settings, "SOAP_PROXY_ADDRESS", defaults.SOAP_PROXY_ADDRESS), username=getattr(settings, "SOAP_USERNAME", defaults.SOAP_USERNAME), password=getattr(settings, "SOAP_PASSWORD", defaults.SOAP_PASSWORD))
    print(soap_client)
    try:
        soap_result = eval("soap_client.%s(%s)" % (method.method_call, param_string))
    except Exception, e:
        print(e)
    print(soap_result)
    response = HttpResponse(soap_result, content_type="text/xml")
    return response