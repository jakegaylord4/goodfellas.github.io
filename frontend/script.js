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

