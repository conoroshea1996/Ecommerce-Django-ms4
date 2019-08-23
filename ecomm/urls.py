"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from products.views import all_products
from django.contrib import admin
from django.urls import path, re_path, include
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_carts
from checkout import urls as urls_checkout
from search import urls as urls_search
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', all_products, name='index'),
    re_path(r'^accounts/', include(urls_accounts)),
    re_path(r'^products/', include(urls_products)),
    re_path(r'^cart/', include(urls_carts)),
    re_path(r'^checkout/', include(urls_checkout)),
    re_path(r'^search/', include(urls_search)),
    re_path(r'^media/(?P<path>.*)$', static.serve,
            {'document_root': MEDIA_ROOT}),
]
