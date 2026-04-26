function openLoginForm() {
    closeSignUpForm();
    document.getElementById("loginForm").style.display = "block";
  }
  
  function closeLoginForm() {
    document.getElementById("loginForm").style.display = "none";
  }

function openSignUpForm() {
    closeLoginForm();
    document.getElementById("signupForm").style.display = "block";
  }
  
  function closeSignUpForm() {
    document.getElementById("signupForm").style.display = "none";
  }

let login = () => {
    // TODO: Implement login logic
    const email = document.getElementById("email-login").value;
    const password = document.getElementById("psw-login").value;
    console.log("Login clicked", email, password);
}

let signUp = () => {
    // TODO: Implement sign up logic
    const firstName = document.getElementById("firstname-signup").value;
    const lastName = document.getElementById("lastname-signup").value;
    const email = document.getElementById("email-signup").value;
    const password = document.getElementById("psw-signup").value;
    console.log("Sign up clicked", firstName, lastName, email, password);
}

function openLogoutForm() {
    document.getElementById("logoutForm").style.display = "block";
  }
  
  function closeLogoutForm() {
    document.getElementById("logoutForm").style.display = "none";
  }

const fileInput = document.getElementById('service_image');
if (fileInput) {
    fileInput.addEventListener('change', function () {
        const fileName = this.files[0] ? this.files[0].name : '';
        document.getElementById('file-name').innerText = fileName;
    });
}