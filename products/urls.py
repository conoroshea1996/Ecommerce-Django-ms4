from django.conf.urls import url, include, re_path
from .views import all_products, product


urlpatterns = [
    re_path(r'^$', all_products, name='products'),
    re_path(r'^(?P<product_id>\d+)/$', product, name='product'),
    re_path(r'^(?P<catagory_name>[-\w]+)/$', all_products, name='products'),
]
