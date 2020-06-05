var user = requestUser
var updateBtns = document.getElementsByClassName('update-cart')


for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        if(user == 'AnonymousUser') {
            console.log('user unauthenticated - calling addCookieItem')
            addCookieItem(productId, action)
        } else {
            console.log('user authenticated - calling updateUserItem')
            updateUserItem(productId, action)
        }
    })
}

function addCookieItem(productId, action) {
    console.log('addCookieItem(productId, action):', productId, action)

    if(action == 'add') {
        if(cart[productId] == undefined) {
            cart[productId] = {'quantity':1}
        } else {
            cart[productId]['quantity'] += 1
        }
    }

     if(action == 'remove') {
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId]
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserItem(productId, action) {
    console.log('updateUserItem(productId, action):', productId, action)

    fetch('/update-item/', {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        location.reload()
    })
}

jQuery(function($)
{
    //Scroll to top when button selected
    $('.scrollup').click(function()
    {
        $.scrollTo(0, 1500);
    });

    //Show / hide button depend os position
    $(window).scroll(function()
    {
        if($(this).scrollTop()>500) $('.scrollup').fadeIn();
        else $('.scrollup').fadeOut();
    });
});