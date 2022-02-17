from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



# Register your models here.
from rango.models import Category, Page
#admin.site.register(Category)
admin.site.register(Category, CategoryAdmin)

#admin.site.register(Page)
admin.site.register(Page,PageAdmin)
#在page页面同时显示title，category和url


