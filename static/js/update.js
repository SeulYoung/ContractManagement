function email_check() {
    let email = document.getElementById("email").value;
    let email_valid = /^[0-9a-z\-_]+(\.[0-9a-z\-_]+)*@[0-9a-z]+(\.[0-9a-z]+)+$/;

    if (!email_valid.test(email)) {
        document.getElementById('error').innerHTML = 'enter a valid email address.';
        return false;
    }
    return true;
}

function password_check() {
    let password1 = document.getElementById("password1").value;
    let password2 = document.getElementById("password2").value;

    if (password1.length < 6) {
        document.getElementById("error").innerHTML = "password too short.";
        return false;
    }
    if (password1 !== password2) {
        document.getElementById("error").innerHTML = "password mismatch.";
        return false;
    }
    return true;
}