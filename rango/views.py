from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Page
from rango.models import Category

import rango
"""
def index(request):
    #return HttpResponse("Rango says hey there partner!")
    #return HttpResponse('<a href="http://127.0.0.1:8000/rango/about/">Rango says hey there partner!')
    return HttpResponse("<a href='/rango/about/'>About</a> Rango says hey there partner!")

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}#context_dict里面会有很多东西，所以template里面才会用两层花括号来匹配
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)#很奇怪的是它是自动到template路径下找的
"""
def index(request):
# Query the database for a list of ALL categories currently stored.
# Order the categories by the number of likes in descending order.
# Retrieve the top 5 only -- or all if less than 5.
# Place the list in our context_dict dictionary (with our boldmessage!)
# that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    context_dict['pages'] = page_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)

"""
def about(request):
    #return HttpResponse(""<a href="http://127.0.0.1:8000/">HttpResponse: 'Rango says here is the about page.'"")
    return HttpResponse("<a href='/rango/'>Index</a> Rango says here is the about page.")
"""
def about(request):
    #return HttpResponse("""<a href="http://127.0.0.1:8000/">HttpResponse: 'Rango says here is the about page.'""")
    context_dict = {'boldmessage': 'This tutorial has been put together by YuHeng OuYang'}
    return render(request, 'rango/about.html',context=context_dict)


def show_category(request, category_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}
    try:
    # Can we find a category name slug with the given name?
    # If we can't, the .get() method raises a DoesNotExist exception.
    # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
    # Retrieve all of the associated pages.
    # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
    # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
    # We also add the category object from
    # the database to the context dictionary.
    # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything -
    # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
# Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)