from django.shortcuts import render

from empires.tasks import store_units

# Create your views here.


def index(request):
    """
    - render starter bootstrap template
    - call backgroud task to fetch data from api and store it in local DB

    """
    store_units.delay()
    template_name = 'index.html'
    context = {
    }

    return render(request, template_name, context)
