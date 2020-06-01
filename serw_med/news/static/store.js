var user = requestUser
var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        if(user == 'AnonymousUser') {
            console.log('user unauthenticated - no onclick event')
        } else {
            console.log('user authenticated - calling updateUserItem')
            updateUserItem(productId, action)
        }
    })
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