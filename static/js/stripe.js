console.log('preparing for magic');

$(function() {
    $("#payment-form").submit(function() {
        console.log('doing magic on payment-form');

        var form = this;
        console.log('form ', form);
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $('input.select-dropdown')[1].value,
            expYear: $('input.select-dropdown')[2].value,
            cvc: $("#id_cvv").val()
        };
        console.log('card is ', card)
    
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            // $('input.select-dropdown')[1].removeAttr(':selected');
            // $('input.select-dropdown')[2].removeAttr(':selected');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});