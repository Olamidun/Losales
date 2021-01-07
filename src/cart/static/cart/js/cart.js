// console.log("Hello world")

var updateButtons = document.getElementsByClassName('update-cart')

for( var i = 0;i<=updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(){
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log('ProductId: ', productId, 'Action: ', action)

        if (user === 'AnonymousUser'){
            console.log('User is not logged in')
        } else{
            updateBuyerOrder(productId, action)
        }
        
    })
}

function updateBuyerOrder(productId, action){
    let url = '/cart/update_item'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    }).then((response) => {
        return response.json()
    }).then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}
