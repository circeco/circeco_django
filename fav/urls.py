from django.conf.urls import url
from .views import view_fav, add_to_fav, remove_fav

urlpatterns = [
    url(r'^$', view_fav, name='view_fav'),
    url(r'^add/(?P<shopId>\d+)', add_to_fav, name='add_to_fav'),
    url(r'^remove/(?P<shopId>\d+)', remove_fav, name='remove_fav'),
    url(r'^add/(?P<shopId>\d+)/ws', add_to_fav, name='add_to_fav_ws'),
    url(r'^remove/(?P<shopId>\d+)/ws', remove_fav, name='remove_fav_ws'),
]