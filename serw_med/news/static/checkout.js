var redirectUrl = redirectToStore
var total = cartTotal
var shipping = orderShipping
var user = requestUser
var form = document.getElementById('form')


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

form.addEventListener('submit', function(e){
    e.preventDefault()

    document.getElementById('store-form').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
})

document.getElementById('make-order').addEventListener('click', function(e){
    paymentButton('banktransfer')
})

function paymentButton(payment) {
    console.log('paymentButton(payment):', payment)

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
        userFormData.name = form.login.value
        userFormData.email = form.email.value
    }

    fetch('/process-order/', {
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
        cart = {}
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

        window.location.href = redirectUrl
    })
}