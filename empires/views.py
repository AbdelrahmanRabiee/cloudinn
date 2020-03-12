from django.shortcuts import render

# Create your views here.

def index(request):
    """
    render starter bootstrap template
    """
    template_name = 'index.html'
    context = {}

    return render(request, template_name, context)
    
