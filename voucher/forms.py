from django import forms


class BuyVoucherForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]
    VOUCHER_AMOUNT = [(i, i) for i in [100,200,300]]

    amount = forms.ChoiceField(label='Amount in Swedish kr', choices=VOUCHER_AMOUNT, required=True)

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    
    stripe_id = forms.CharField(widget=forms.HiddenInput)
