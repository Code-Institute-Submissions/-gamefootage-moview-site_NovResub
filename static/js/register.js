$("#password, #confirm-password").on("keyup", function(e) {
  if ($("#password").val() !== $("#confirm-password").val()) {
    $("#confirm-password").get(0).setCustomValidity('Password fields must match');
  } else if ($("#password").val().length > 4 && $("#confirm-password").val().length > 4) {
    $("#confirm-password").get(0).setCustomValidity('');
  } else {
    $("#password").get(0).setCustomValidity('Must be 5 characters in length'); 
  }
});

$("#username").on("keypress", function(e) {
  const key = e.keyCode;
  if (key === 32) {
    e.preventDefault();
  }
});