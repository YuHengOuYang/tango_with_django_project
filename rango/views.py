from django.shortcuts import render
from django.http import HttpResponse

import rango

def index(request):
    #return HttpResponse("Rango says hey there partner!")
    #return HttpResponse('<a href="http://127.0.0.1:8000/rango/about/">Rango says hey there partner!')
    return HttpResponse("<a href='/rango/about/'>About</a> Rango says hey there partner!")
def about(request):
    #return HttpResponse("""<a href="http://127.0.0.1:8000/">HttpResponse: 'Rango says here is the about page.'""")
    return HttpResponse("<a href='/rango/'>Index</a> Rango says here is the about page.")