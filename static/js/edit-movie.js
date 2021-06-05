$(document).ready(function() {
  let str = $("#starring").val()
  let arr = str.split(",")
  let data = arr.reduce(function(obj, a){
    obj.push({tag: a});
    return obj;
  }, [])
  
  $('.chips-placeholder').chips({
    placeholder: "Enter an actor",
    secondaryPlaceholder: '+Actor',
  });
  $('.chips-initial').chips({
    data: data
  });
})

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
})