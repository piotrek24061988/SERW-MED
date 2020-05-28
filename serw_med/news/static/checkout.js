var redirectUrl = redirectToStore
var total = cartTotal
var shipping = '{{ order.shipping }}'
var user = '{{ request.user }}'

if(shipping == 'False') {
    document.getElementById('shipping-info').innerHTML = ''
}

if(user != 'AnonymousUser') {
    document.getElementById('user-info').innerHTML = ''
}

if(shipping == 'False' && user != 'AnonymousUser') {
    document.getElementById('form-wrapper').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
}

var form = document.getElementById('form')

form.addEventListener('submit', function(e){
    e.preventDefault()

    document.getElementById('store-form').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
})

document.getElementById('make-payment').addEventListener('click', function(e){
    paymentButton('paypal')
})

document.getElementById('make-order').addEventListener('click', function(e){
    paymentButton('banktransfer')
})

function paymentButton(payment) {

    var userFormData = {
        'name': null,
        'email': null,
        'total': total,
        'payment': payment
    }

    var userShippingInfo = {
        'adres': null,
        'kod': null,
        'miasto': null,
        'telefon':null
    }

    if(shipping != 'False') {
        userShippingInfo.adres = form.adres.value
        userShippingInfo.kod = form.kod.value
        userShippingInfo.miasto = form.miasto.value
        userShippingInfo.telefon = form.telefon.value
    }

    if(user == 'AnonymousUser') {
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }

    var url = '/process-order/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'userShippingInfo': userShippingInfo, 'userFormData': userFormData})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        window.location.href = redirectUrl
    })
}