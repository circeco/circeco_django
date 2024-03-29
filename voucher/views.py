from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from voucher.models import Voucher
import stripe
import http.client
from django.contrib import messages
from .forms import BuyVoucherForm
from circeco_django import settings
import json
from django.http.response import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
import os

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def choose_voucher(request): 
    form = BuyVoucherForm()
    return render(request, 'choose_voucher.html', {"form": form, "publishable": settings.STRIPE_PUBLISHABLE})


@login_required()
def create_voucher(request):
    user = request.user
    form = BuyVoucherForm(request.POST)
    print(form)
    amount = int(form.cleaned_data['amount'])

    try:
        customer = stripe.Charge.create(
            amount=100*amount,
            currency="SEK",
            description=request.user.email,
            card=form.cleaned_data['stripe_id']
        )
    except stripe.error.CardError:
        messages.error(request, "Your card was declined!")
    
    if customer.paid:
        messages.error(request, "You have successfully paid")

        newVoucher = Voucher(user=user, amount=amount)       
        newVoucher.save() 
        
        return redirect(reverse('profile'))
    else:
        messages.error(request, "Unable to take payment")

    return render(request, 'choose_voucher.html', {"form": form, "publishable": settings.STRIPE_PUBLISHABLE})


@login_required()
def display_QR(request, id):
    try:
        voucher = Voucher.objects.get(id=id)
    except:
        return HttpResponseNotFound("Voucher not found!")
    
    if request.user != voucher.user:
        print(f'naughty user {request.user} trying to read what belongs to {voucher.user}')
        return HttpResponseForbidden("Naughty, naughty!")
        
    if voucher.image == None:
        hostname = os.environ.get('HOSTNAME')
        relative = reverse('verify_voucher', args=(voucher.id,))
        image = makeQR(f'https://{hostname}{relative}') 
        voucher.image = image
        voucher.save() 

    return HttpResponse(voucher.image, content_type='image/png')


def verify_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    return render(request, 'verify_voucher.html', {"voucher": voucher})


def makeQR(myData):
    conn = http.client.HTTPSConnection("qrcode-monkey.p.rapidapi.com")

    p = {
        "data":myData,
        "config":{
            "body":"japnese",
            "eye":"frame5",
            "eyeBall":"ball11",
            "erf1":['fh'],
            "erf2":[],
            "erf3":['fv','fh'],
            "brf1":['fh'],
            "brf2":[],
            "brf3":['fv','fh'],
            "bodyColor":"#204047",
            "bgColor":"#FFFFFF",
            "eye1Color":"#FF5252",
            "eye2Color":"#FF5252",
            "eye3Color":"#FF5252",
            "eyeBall1Color":"#134f5cff",
            "eyeBall2Color":"#134f5cff",
            "eyeBall3Color":"#134f5cff",
            "gradientColor1":"#0c343dff",
            "gradientColor2":"#0c343dff",
            "gradientType":"linear",
            "gradientOnEyes":False,
            },
        "size":600,
        "download":False,
        "file":"png"
    }
    
    payload = json.dumps(p)

    headers = {
        'x-rapidapi-host': "qrcode-monkey.p.rapidapi.com",
        'x-rapidapi-key': "02ee0a6910msh7ab1091612dfbacp185d5ejsnfcc7e4d94ae1",
        'content-type': "application/json",
        'accept': "application/json"
        }

    conn.request("POST", "/qr/custom", payload, headers)

    return conn.getresponse().read() 