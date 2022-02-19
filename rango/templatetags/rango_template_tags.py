from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')#看不懂,貌似是把函数返回值绑定到渲染页上，插入渲染页到调用函数的目标template中去
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}


"""
This new template is used by the Django template engine to render
the list of categories you provide in the dictionary that is returned in the function.
This rendered list can then be injected into the response of the view that initially
called the template tag!
"""
