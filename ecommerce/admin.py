from django.contrib import admin
from . import models

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.brand, BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.category,CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','description','price')

admin.site.register(models.products, ProductsAdmin)
admin.site.register(models.profile)
admin.site.register(models.cart)