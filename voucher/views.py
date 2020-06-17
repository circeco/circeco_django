from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from voucher.models import Voucher
import stripe
from django.contrib import messages
from .forms import BuyVoucherForm
from circeco_django import settings


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
        return redirect(reverse('voucher'))
    else:
        messages.error(request, "Unable to take payment")


    newVoucher = Voucher(user=user, amount=amount)
    newVoucher.save()
    print(newVoucher.id)

    return render(request, 'view_voucher.html', {"voucher": newVoucher})
