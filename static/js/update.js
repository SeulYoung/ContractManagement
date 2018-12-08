function email_check() {
    let email = document.getElementById("email").value;
    let email_valid = /^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$/;

    if (!email_valid.test(email)) {
        document.getElementById('error').innerHTML = 'enter a valid email address.';
        return false;
    }
    return true;
}

function password_check() {
    let password = document.getElementById("password").value;
    let password_confirmation = document.getElementById("password_confirmation").value;

    if (password.length < 6) {
        document.getElementById("error").innerHTML = "password too short.";
        return false;
    }
    if (password !== password_confirmation) {
        document.getElementById("error").innerHTML = "password mismatch.";
        return false;
    }
    return true;
}