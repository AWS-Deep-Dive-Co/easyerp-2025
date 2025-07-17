from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):

    html = "<html><body>Hello {}!</body></html>".format('solar system')
    return HttpResponse(html)