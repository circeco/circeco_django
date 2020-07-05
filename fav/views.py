from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import UserFavouriteShop
from shops.models import Shop
from django.http import HttpResponse
from http import HTTPStatus
from django.views.decorators.http import require_http_methods


@login_required()
def view_fav(request):
    """A View that renders the fav contents page"""
    favs = UserFavouriteShop.objects.all().filter(user = request.user) # TODO "project" only shop 
    return render(request, "fav.html", {"fav_items": favs})

@login_required()
def add_to_fav(request, shopId):
    """Add a selected shop to the user's favourite list"""

    userId = request.user
    # TODO associate userId and shopId

    print(shopId, userId)

    shop = Shop.objects.get(id=shopId) # TODO handle exception
    newFav = UserFavouriteShop(user=userId, shop=shop)
    newFav.save()

    print(newFav.id)

    return redirect(reverse('view_fav'))

@login_required()
def remove_fav(request, shopId):
    """Remove a selected shop from the user's favourite list"""
    
    shop = Shop.objects.get(id=shopId)
    afav = UserFavouriteShop.objects.get(user=request.user, shop=shop) # TODO handle exception
    afav.delete() 

    return redirect(reverse('profile'))

@login_required()
@require_http_methods(["PUT"])
def add_to_fav_ws(request, shopId):
    """Add a selected shop to the user's favourite list"""

    userId = request.user

    shop = Shop.objects.get(id=shopId) # TODO handle exception
    newFav = UserFavouriteShop(user=userId, shop=shop)
    newFav.save()

    return HttpResponse(status_code = HTTPStatus.NO_CONTENT)

@login_required()
@require_http_methods(["PUT"])
def remove_fav_ws(request, shopId):
    """Remove a selected shop from the user's favourite list"""
    
    shop = Shop.objects.get(id=shopId)
    afav = UserFavouriteShop.objects.get(user=request.user, shop=shop) # TODO handle exception
    afav.delete() 

    return HttpResponse(status_code = HTTPStatus.NO_CONTENT)