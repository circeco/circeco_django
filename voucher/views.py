from django.shortcuts import redirect, render
from django.urls.base import reverse
from voucher.models import Voucher


# Create your views here.
def choose_voucher(request): 
    return render(request, 'choose_voucher.html')


def create_voucher(request):
    """xxx"""

    user = request.user
    print(user)
    if user.is_authenticated:
        print('authenticated')
    else:
        print('NOT authenticated')
        
    amount = request.POST.get('amount')
    print(f'create voucher user={user} amount={amount}')

    # TODO payment

    newVoucher = Voucher(user=user, amount=amount)
    newVoucher.save()
    print(newVoucher.id)

    return render(request, 'view_voucher.html', {"voucher": newVoucher})
