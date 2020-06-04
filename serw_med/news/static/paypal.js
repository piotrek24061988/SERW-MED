var total = cartTotal

paypal.Buttons({

    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: parseFloat(total).toFixed(2)
                }
            }]
        });
    },

    onApprove: function(data, actions) {
        return actions.order.capture().then(function(detail) {
            paymentButton('paypal')
        });
    }

}).render('#paypal-button-container');