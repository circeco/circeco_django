from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from voucher.models import Voucher


@login_required()
def choose_voucher(request): 
    return render(request, 'choose_voucher.html')


@login_required()
def create_voucher(request):
    """xxx"""

    user = request.user
    amount = request.POST.get('amount')
    print(f'create voucher user={user} amount={amount}')

    # TODO payment

    newVoucher = Voucher(user=user, amount=amount)
    newVoucher.save()
    print(newVoucher.id)

    return render(request, 'view_voucher.html', {"voucher": newVoucher})
