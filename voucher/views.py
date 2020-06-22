from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from voucher.models import Voucher
import stripe
from django.contrib import messages
from .forms import BuyVoucherForm
from circeco_django import settings

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def choose_voucher(request): 
    # TODO instantiate form and pass it to rendering
    form = BuyVoucherForm()
    return render(request, 'choose_voucher.html', {"form": form, "publishable": settings.STRIPE_PUBLISHABLE})


@login_required()
def create_voucher(request):
    """xxx"""

    user = request.user
    form = BuyVoucherForm(request.POST)
    print(form)

    # amount = request.POST.get('amount')
    #print(f'create voucher user={user} amount={amount}')
    amount = int(form.cleaned_data['amount'])

    try:
        customer = stripe.Charge.create(
            amount=amount,
            currency="SEK",
            description=request.user.email,
            card=form.cleaned_data['stripe_id']
        )
    except stripe.error.CardError:
        messages.error(request, "Your card was declined!")
    
    if customer.paid:
        messages.error(request, "You have successfully paid")

        # Save voucher here 
        newVoucher = Voucher(user=user, amount=amount)
        newVoucher.save()
        print(newVoucher.id)

        targetUrl = request.build_absolute_uri(reverse('verify_voucher', args=(newVoucher.id,)))
        # TODO This should be the URL that goes into the QR

        return render(request, 'view_voucher.html', {"voucher": newVoucher, "targetUrl": targetUrl})
    else:
        messages.error(request, "Unable to take payment")

    # If we get here there has been no payment!

    return render(request, 'choose_voucher.html', {"form": form, "publishable": settings.STRIPE_PUBLISHABLE})


# login not required
def verify_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    return render(request, 'verify_voucher.html', {"voucher": voucher})
