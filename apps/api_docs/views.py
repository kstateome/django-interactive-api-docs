from django.shortcuts import render
from api_docs.models import *

def home(request):
    context = {'apis':APIDoc.objects.all()}
    return render(request, 'api_docs/apis.html', context)
    