from django.conf.urls import url, include
from .views import all_shops

urlpatterns = [
    url(r'^$', all_shops, name='shops'),
]