$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.materialboxed').materialbox();
  $(".dropdown-trigger").dropdown();
  $('.chips').chips();
});

$("#snackbar").on("click", function() {
  $("#snackbar").removeClass("show");
});