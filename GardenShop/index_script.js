var cart = []

//Go to login page
function redirectToLogin() {
	window.location.href = "http://localhost:8080/login_page.html";
}

//Update number of items in cart
function updateNumItemsCart() {
	text = document.getElementById("itemsNum");
	text.innerHTML = "Number of items in cart: " + cart.length;
}

function openProperPage(page) {
	window.location.href = page;
}

//Look the cart
function accessCart() {
	console.log("sending cart");
	console.log(cart);
	var myJSON = JSON.stringify(cart);
	console.log(myJSON);
	httpGetAsync("http://localhost:8080/carts/cart.html", myJSON, openProperPage);
}

//Function to make HTTP requests
function httpGetAsync(url, info, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", url, true); // true for asynchronous 
    xmlHttp.send(info);
}

//Adding products to cart
function addPurpleRose() {
	cart.push("purpleRose");
	updateNumItemsCart();
	console.log(cart);
}

function addPinkRose() {
	cart.push("pinkRose");
	updateNumItemsCart();
	console.log(cart);
}

function addViolet() {
	cart.push("violet");
	updateNumItemsCart();
	console.log(cart);
}

function addNormalPlant() {
	cart.push("normalPlant");
	updateNumItemsCart();
	console.log(cart);
}

function addBamboo() {
	cart.push("bamboo");
	updateNumItemsCart();
	console.log(cart);
}

function addGrassPlant() {
	cart.push("grassPlant");
	updateNumItemsCart();
	console.log(cart);
}

function addVase() {
	cart.push("vase");
	updateNumItemsCart();
	console.log(cart);
}

function addScissor() {
	cart.push("scissor");
	updateNumItemsCart();
	console.log(cart);
}

function addWateringCan() {
	cart.push("wateringCan");
	updateNumItemsCart();
	console.log(cart);
}