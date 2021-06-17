$("#password, #confirm-password").on("keyup", function(e) {
  if ($("#password").val() !== $("#confirm-password").val()) {
    $("#confirm-password").get(0).setCustomValidity('Password fields must match');
  } else if ($("#password").val().length > 5 && $("#confirm-password").val().length > 5) {
    $("#confirm-password").get(0).setCustomValidity('');
  }
});

$("#username").on("keypress", function(e) {
  const key = e.keyCode;
  if (key === 32) {
    e.preventDefault();
  }
});