from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')


# Register your models here.
from rango.models import Category, Page
admin.site.register(Category)
#admin.site.register(Page)
admin.site.register(Page,PageAdmin)
#在page页面同时显示title，category和url


