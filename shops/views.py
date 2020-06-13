from django.shortcuts import render, redirect, reverse
from .models import Shop

# Create your views here.
def all_shops(request):
    shops = Shop.objects.all()
    return render(request, "shops.html", {"shops": shops})
