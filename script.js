function showAuthForm() {
    document.getElementById('landing-page').style.display = 'none';
    document.getElementById('auth-form').style.display = 'block';
}

function toggleForm(form) {
    if (form === 'signup') {
        document.getElementById('login-form').style.display = 'none';
        document.getElementById('signup-form').style.display = 'block';
    } else {
        document.getElementById('signup-form').style.display = 'none';
        document.getElementById('login-form').style.display = 'block';
    }
}

function loginUser(event) {
    event.preventDefault();
    document.getElementById('auth-form').style.display = 'none';
    document.getElementById('sidebar').style.display = 'block';
    document.getElementById('dashboard').style.display = 'block';
}

function logout() {
    document.getElementById('sidebar').style.display = 'none';
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('landing-page').style.display = 'flex';
}

function showResetPasswordForm() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('reset-password-form').style.display = 'block';
}

function showLoginForm() {
    document.getElementById('reset-password-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}

function resetPassword(event) {
    event.preventDefault();
    document.getElementById('reset-password-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}