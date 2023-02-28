const switchers = [...document.querySelectorAll('.switcher')]

switchers.forEach(item => {
	item.addEventListener('click', function() {
		switchers.forEach(item => item.parentElement.classList.remove('is-active'))
		this.parentElement.classList.add('is-active')
	})
})

function pass_check(){
	var passwd = document.getElementById('signup-password').value;
	var confirm_passwd = document.getElementById('signup-password-confirm').value;
	document.getElementById("btn-signup").disabled = true; 

	if (passwd != confirm_passwd){
		document.getElementById('passwd-mismatch').innerHTML = "Password doesn't match";
	}
	else if (passwd == "" || confirm_passwd == ""){
		document.getElementById("btn-signup").disabled = true; 
	}
	else{
		document.getElementById('passwd-mismatch').innerHTML = "Password matched";
		document.getElementById('passwd-mismatch').style.color = "green";

		document.getElementById("btn-signup").disabled = false; 
	}

}