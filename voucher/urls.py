from django.conf.urls import url, include
from .views import choose_voucher, create_voucher, verify_voucher

urlpatterns = [
    url(r'^$', choose_voucher, name='choose_voucher'),
    url(r'^create/', create_voucher, name='create_voucher'),
    url(r'^verify/(?P<id>\d+)', verify_voucher, name='verify_voucher'),
]