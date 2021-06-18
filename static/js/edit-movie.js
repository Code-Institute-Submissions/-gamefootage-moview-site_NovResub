$(document).ready(function() {
  let str = $("#starring").val()
  if (str) {
    let arr = str.split(",")
    let data = arr.reduce(function(obj, a){
      obj.push({tag: a});
      return obj;
    }, [])

    $('.chips-initial').chips({
      data: data
    });
    
  }

  $('.chips-placeholder').chips({
    placeholder: "Press the enter key after the typing the actor's name",
    secondaryPlaceholder: '+Actor',
  });
  
});

$("button[name=edit-movie-btn]").on("click", function() {
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

  $("#edit-movie-form").submit();
});

$("#cover_image_url").on("keyup", function() {
  if ($("#cover_image_url").val().match(/\.(jpeg|jpg|png)$/) == null) {
    $("#cover_image_url").get(0).setCustomValidity('Must be a valid URL of JPEG, JPG or PNG format.');
  } else {
    $("#cover_image_url").get(0).setCustomValidity('');
  }
});