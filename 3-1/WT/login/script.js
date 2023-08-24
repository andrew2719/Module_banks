document.getElementById('show-register').addEventListener('click', function() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('register-container').style.display = 'block';
});

document.getElementById('show-login').addEventListener('click', function() {
    document.getElementById('register-container').style.display = 'none';
    document.getElementById('login-container').style.display = 'block';
});

// For Google OAuth, you'd typically use a library or SDK provided by Google. This is just a placeholder.
document.getElementById('google-login').addEventListener('click', function() {
    alert('Google OAuth functionality to be implemented.');
});

document.getElementById('google-register').addEventListener('click', function() {
    alert('Google OAuth functionality to be implemented.');
});
