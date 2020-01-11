function ValidateEmail(inputText){
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(inputText.value.match(mailformat)){
		document.getElementById("mail").style.display = "none";
		document.register.email.focus();
		return true;
	}
	else{
		document.getElementById("mail").style.display = "block";
		document.register.email.focus();
		return false;
	}
}
function PasswordSecurity(inputText){
	if(inputText.value.length < 8){
		document.getElementById("pass").style.display = "block";
		document.register.password.focus();
		return false;
	}
	else{
		document.getElementById("pass").style.display = "none";
		document.register.password.focus();
		return true;
	}
}
function PasswordMatch(str1, str2){
	var n = str1.toString().localeCompare(str2);
	if(n != 0){
		document.getElementById("pass2").style.display = "none";
		return true;
	}
	else{
		document.getElementById("pass2").style.display = "block";	
		return false;
	}
}
function Validation(){
	if(PasswordSecurity(document.register.password) &&
	ValidateEmail(document.register.email) &&
	PasswordMatch(document.register.password, document.register.confirmPassword)){
		return true;
	}
	return false;
}

