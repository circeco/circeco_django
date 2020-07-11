from django.conf.urls import url, include
from .views import all_shops, search


urlpatterns = [
    url(r'^$', all_shops, name='shops'),
    url(r'^search/', search, name='search'),
]