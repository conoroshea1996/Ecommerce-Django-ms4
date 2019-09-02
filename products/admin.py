from django.contrib import admin
from .models import Product, Catagory, Photo, Brand
# Register your models here.
admin.site.register(Catagory)
admin.site.register(Brand)


class ImageInline(admin.TabularInline):
    model = Photo
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Product, ProductAdmin)
