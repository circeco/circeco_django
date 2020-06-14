from django.shortcuts import render, redirect, reverse
from .models import UserFavouriteShop
from shops.models import Shop


# Create your views here.
def view_fav(request):
    """A View that renders the fav contents page"""
    favs = UserFavouriteShop.objects.all().filter(user = request.user) # TODO "project" only shop 
    return render(request, "fav.html", {"fav_items": favs})


def add_to_fav(request, shopId):
    """xxx"""

    userId = request.user
    # TODO associate userId and shopId

    print(shopId, userId)

    shop = Shop.objects.get(id=shopId) # TODO handle exception
    newFav = UserFavouriteShop(user=userId, shop=shop)
    newFav.save()

    print(newFav.id)

    return redirect(reverse('view_fav'))


def remove_fav(request, shopId):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    
    shop = Shop.objects.get(id=shopId)
    afav = UserFavouriteShop.objects.get(user=request.user, shop=shop) # TODO handle exception
    afav.delete() 

    return redirect(reverse('view_fav'))