$("#profile_url").on("keyup", function() {
  if ($("#profile_url").val().match(/\.(jpeg|jpg|png)$/) == null) {
    $("#profile_url").get(0).setCustomValidity('Must be a valid URL of JPEG, JPG or PNG format.');
  } else {
    $("#profile_url").get(0).setCustomValidity('');
  }
});