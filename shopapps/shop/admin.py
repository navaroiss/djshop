from django.contrib import admin
from djshop.shopapps.shop.models import *

class AdminCategory(admin.ModelAdmin):
    list_display = ('catname', 'catparent')
    class Media:
        pass
admin.site.register(Category, AdminCategory)

class AdminProduct(admin.ModelAdmin):
    class Media:
        js = ('http://localhost/skin/templates/media/js/tiny_mce/tiny_mce.js',
              'http://localhost/skin/templates/media/js/editor.js')
admin.site.register(Product, AdminProduct)

class AdminImage(admin.ModelAdmin):
    pass
admin.site.register(Image, AdminImage)