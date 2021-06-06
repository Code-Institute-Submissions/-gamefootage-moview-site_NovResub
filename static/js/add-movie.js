$(document).ready(function() {
  $('.chips-placeholder').chips({
    placeholder: "Enter an actor",
    secondaryPlaceholder: '+Actor',
  });
});

$("button[name=add-movie-btn]").on("click", function() {
  let actors = [];
  $(".chip").each(function() {
    let s = $(this).text();
    // remove last 5 characters from text (which is material icon 'close') - credit:
    //  https://stackoverflow.com/questions/952924/javascript-chop-slice-trim-off-last-character-in-string
    s = s.substring(0, s.length - 5);
    actors.push(s);
  })
  let str = actors.join(",")
  $("#starring").val(str);

  $("#add-movie-form").submit();
});

$("#cover_image_url").on("keyup", function() {
  if ($("#cover_image_url").val().match(/\.(jpeg|jpg|png)$/) == null) {
    $("#cover_image_url").get(0).setCustomValidity('Must be a valid URL of JPEG, JPG or PNG format.');
  } else {
    $("#cover_image_url").get(0).setCustomValidity('');
  }
});