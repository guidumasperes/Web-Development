function loginPage() {
	var email = document.getElementById("email");
	var pass = document.getElementById("pass");
	var myObj = {e_mail: email.value, password: pass.value};
	var myJSON = JSON.stringify(myObj);
	httpGetAsync("http://localhost:8080/my_user_page.html", myJSON, openProperPage);
}

function httpGetAsync(url, info, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", url, true); // true for asynchronous 
    xmlHttp.send(info);
}

function createConfirmation() {
	var email = document.getElementById("email");				         // Obtain email and password from input
	var pass = document.getElementById("pass");
	var myObj = {e_mail: email.value, password: pass.value};  			// Create json
	var myJSON = JSON.stringify(myObj);
	httpGetAsync("http://localhost:8080", myJSON, openProperPage);		// Send email and pass
}

function openProperPage(page) {
	window.location.href = page;
}