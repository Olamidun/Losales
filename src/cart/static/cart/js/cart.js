// console.log("Hello world")

var updateButtons = document.getElementsByClassName('update-cart')

for( var i = 0; i<=updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(e){
        e.preventDefault()
        let productId = this.dataset.product
        let action = this.dataset.action
    
        console.log('ProductId: ', productId, 'Action: ', action)

        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
        } else{
            updateBuyerOrder(productId, action)
        }
        
    })
}


function addCookieItem(productId, action){
	// console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
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
        console.log(csrftoken)
        location.reload()
    })
}

