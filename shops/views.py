from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Shop
from fav.models import UserFavouriteShop


@login_required()
@ensure_csrf_cookie
def all_shops(request):
    shops = Shop.objects.all()
    favs = UserFavouriteShop.objects.all().filter(user = request.user) 
    favShopIds = set()
    for fav in favs: 
        favShopIds.add(fav.shop.id) 
    return render(request, "shops.html", {"shops": shops, "favs": favShopIds})
