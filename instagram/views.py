from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    name = 'instagram app'

    return render(request, 'index.html', {"name":name})
