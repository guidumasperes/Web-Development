function openProperPage(page) {
	window.location.href = page;
}

//Function to make HTTP requests
function httpGetAsync(url, info, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", url, true);
    xmlHttp.send(info);
}

//Remove products to cart
function purpleRoseRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["purpleRose"]), openProperPage)
}

function pinkRoseRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["pinkRose"]), openProperPage)
}

function violetRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["violet"]), openProperPage)
}

function normalPlantRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["normalPlant"]), openProperPage)
}

function bambooRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["bamboo"]), openProperPage)
}

function grassPlantRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["grassPlant"]), openProperPage)
}

function vaseRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["vase"]), openProperPage)
}

function scissorRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["scissor"]), openProperPage)
}

function wateringCanRemoval() {
	httpGetAsync("http://localhost:8080/updated_cart.html", JSON.stringify(["wateringCan"]), openProperPage)
}