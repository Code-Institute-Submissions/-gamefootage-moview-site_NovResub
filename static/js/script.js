$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.materialboxed').materialbox();
  $(".dropdown-trigger").dropdown();
  $('.chips').chips();
  $('.modal').modal();
});

$("#snackbar").on("click", function() {
  $("#snackbar").removeClass("show");
});