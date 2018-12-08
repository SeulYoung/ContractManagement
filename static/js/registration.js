function register_check() {
    let email = document.getElementById("email").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let password_confirmation = document.getElementById("password_confirmation").value;
    let email_valid = /^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$/;
    let username_valid = /^[a-z]+$/;

    if (!email_valid.test(email)) {
        document.getElementById('error').innerHTML = 'enter a valid email address.';
        return false;
    }
    if (!username_valid.test(username)) {
        document.getElementById('error').innerHTML = 'username has illegal characters.';
        return false;
    }
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