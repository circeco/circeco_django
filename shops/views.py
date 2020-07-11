from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Shop
from fav.models import UserFavouriteShop
from .forms import SearchShopsForm
from django.http import HttpResponse
from django.db.models import Q


@login_required()
@ensure_csrf_cookie
def all_shops(request):
    shops = Shop.objects.all()
    favs = UserFavouriteShop.objects.all().filter(user = request.user) 
    favShopIds = set()
    for fav in favs: 
        favShopIds.add(fav.shop.id) 
    return render(request, "shops.html", {"shops": shops, "favs": favShopIds})


def search(request): 
    form = SearchShopsForm(request.POST)
    form.is_valid() # This is necessary to get clean data
    term = form.cleaned_data['term']
    found = Shop.objects.filter(Q(serviceType__contains=term) | Q(description__contains=term) | Q(name__contains=term))

    favs = UserFavouriteShop.objects.all().filter(user = request.user) 
    favShopIds = set()
    for fav in favs: 
        favShopIds.add(fav.shop.id) 

    return render(request, "shops.html", {"shops": found, "favs": favShopIds})

