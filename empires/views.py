import requests
import json

from django.shortcuts import render

from empires.tasks import hello

# Create your views here.

def index(request):
    """
    render starter bootstrap template

    """

    # call celery task
    hello.delay()    
    
    template_name = 'index.html'
    context = {
    }

    return render(request, template_name, context)
    
