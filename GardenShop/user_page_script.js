function httpGetAsync(url, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", url, true); // true for asynchronous 
    xmlHttp.send();
}

function openProperPage(page) {
	window.location.href = page;
}

function logout() {
	httpGetAsync("http://localhost:8080/logout_page.html", openProperPage);
}