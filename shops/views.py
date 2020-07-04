from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Shop


@login_required()
@ensure_csrf_cookie
def all_shops(request):
    shops = Shop.objects.all()
    return render(request, "shops.html", {"shops": shops})
