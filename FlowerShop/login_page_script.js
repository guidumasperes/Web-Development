function loginPage() {
	console.log("Redirect to Welcome!");
}

function createConfirmation() {
	var email = document.getElementById("email");
	var pass = document.getElementById("pass");
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "http://localhost:8080", true);
	xhttp.setRequestHeader("Content-type", "text/html");
	xhttp.send(email.value+pass.value);
	child = document.getElementById("child");
	var parEmail = document.createElement("p");
	var parPass = document.createElement("p");
	var group = document.createElement("div");
	parEmail.innerHTML = "Your email is: " + email.value
	parPass.innerHTML = "Your password is: " + pass.value
	group.appendChild(parEmail);
	group.appendChild(parPass);
	var header = document.getElementById("header");
	child.innerHTML = group.innerHTML;
	header.innerHTML = "Account created!";
}