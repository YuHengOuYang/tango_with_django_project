from django.shortcuts import render
from django.http import HttpResponse

import rango
"""
def index(request):
    #return HttpResponse("Rango says hey there partner!")
    #return HttpResponse('<a href="http://127.0.0.1:8000/rango/about/">Rango says hey there partner!')
    return HttpResponse("<a href='/rango/about/'>About</a> Rango says hey there partner!")
"""
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}#context_dict里面会有很多东西，所以template里面才会用两层花括号来匹配
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)#很奇怪的是它是自动到template路径下找的


"""
def about(request):
    #return HttpResponse(""<a href="http://127.0.0.1:8000/">HttpResponse: 'Rango says here is the about page.'"")
    return HttpResponse("<a href='/rango/'>Index</a> Rango says here is the about page.")
"""
def about(request):
    #return HttpResponse("""<a href="http://127.0.0.1:8000/">HttpResponse: 'Rango says here is the about page.'""")
    context_dict = {'boldmessage': 'This tutorial has been put together by YuHeng OuYang'}
    return render(request, 'rango/about.html',context=context_dict)