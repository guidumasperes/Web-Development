function loginPage() {
	console.log("Redirect to Welcome!");
}

function createConfirmation() {
	var email = document.getElementById("email");				 // Obtain email and password from input
	var pass = document.getElementById("pass");
	var myObj = {e_mail: email.value, password: pass.value};  			// Create json
	var myJSON = JSON.stringify(myObj);
	var xhttp = new XMLHttpRequest();             					    // Prepare http request to server
	xhttp.onreadystatechange = function() {
    	if(this.readyState === 4 && this.status === 200) {
    		if(this.responseText === "No") {
      			child = document.getElementById("child");
      			var neg = document.createElement("p");
      			neg.innerHTML = "This account already exists";
      			child.innerHTML = neg.innerHTML;
      			var header = document.getElementById("header");
      			header.innerHTML = "Account not created!";
    		} else {
    			child = document.getElementById("child");    // Set variables to do account creation confirmation
				var parEmail = document.createElement("p");
				var parPass = document.createElement("p");
				var group = document.createElement("div");
				parEmail.innerHTML = "Your email is: " + email.value;
				parPass.innerHTML = "Your password is: " + pass.value;
				group.appendChild(parEmail);
				group.appendChild(parPass);
				var header = document.getElementById("header");
				child.innerHTML = group.innerHTML;  				// Confirm the account creation
				header.innerHTML = "Account created!";
			}
		}
  	};
	xhttp.open("POST", "http://localhost:8080", false);
	xhttp.send(myJSON);  											// Send email and pass
}