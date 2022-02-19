from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

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
admin.site.register(UserProfile)#想知道注册的意义是什么，别的py页面也这么写还是单纯admin要这么写？

