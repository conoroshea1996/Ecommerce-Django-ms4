from django.conf.urls import re_path
from .views import do_search

urlpatterns = [
    re_path(r'^$', do_search, name='search')
]
