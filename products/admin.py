from django.contrib import admin
from .models import Product, Catagory, Photo
# Register your models here.
admin.site.register(Catagory)


class ImageInline(admin.TabularInline):
    model = Photo
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Product, ProductAdmin)
