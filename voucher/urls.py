from django.conf.urls import url, include
from .views import choose_voucher, create_voucher, verify_voucher, display_QR

urlpatterns = [
    url(r'^$', choose_voucher, name='choose_voucher'),
    url(r'^create/', create_voucher, name='create_voucher'),
    url(r'^display/(?P<id>\d+)', display_QR, name='voucher'),
    url(r'^verify/(?P<id>\d+)', verify_voucher, name='verify_voucher'),
]