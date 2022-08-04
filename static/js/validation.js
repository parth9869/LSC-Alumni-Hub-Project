function checkEmail() {
    document.getElementById('emailError').style.display="none";
    var email = document.getElementById('email');
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if (!filter.test(email.value)) {
    document.getElementById('emailError').style.display="block";
    email.focus();
    return false;
 }
 return true;
}

function checkMobile()
{
    document.getElementById('mobileError').style.display="none";
    var mobile = document.getElementById('mobileNumber');
    var filter = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;

    if (!filter.test(mobile.value)) {
        document.getElementById('mobileError').style.display="block";
        mobile.focus();
        return false;
}
return true;
}

function validation(){

    if(checkEmail() && checkMobile()){
        return true;
    }
    return false;
}