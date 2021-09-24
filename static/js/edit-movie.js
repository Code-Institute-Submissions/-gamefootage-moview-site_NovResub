$(document).ready(function() {
    $('.chips-placeholder').chips({
      placeholder: "Press the enter key after the typing the actor's name",
      secondaryPlaceholder: '+Actor',
    });

    let str = $("#starring").val();
    console.log(str);
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

    if (formValidate()) {
        $("#edit-movie-form").submit();
    }
});

$("#cover_image_url").on("keyup", delay(function() {
    $("#cover_image_url").get(0).setCustomValidity('Must be a valid URL of JPEG, JPG or PNG format.');
    checkImage($("#cover_image_url").val());
}, 600));
  
  
// Delay action and rollback if called
// Taken from (https://stackoverflow.com/questions/1909441/how-to-delay-the-keyup-handler-until-the-user-stops-typing)
function delay(callback, ms) {
var timer = 0;
return function() {
    var context = this, args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
    callback.apply(context, args);
    }, ms || 0);
};
}

// Check if user submitted url is an image
// taken from (https://stackoverflow.com/questions/55880196/is-there-a-way-to-easily-check-if-the-image-url-is-valid-or-not/55880263)
function checkImage(url) {
console.log("1");
var s = document.createElement("IMG");
s.src = url
s.onerror = function(){
    $("#cover_image_url").get(0).setCustomValidity('Must a readable url pointing to an image.');
}
s.onload = function(){
    $("#cover_image_url").get(0).setCustomValidity('');
}
}

// Form Validation
function formValidate() {
    let valid = true;
    const $requiredInputs = $('input,textarea,select').filter('[required]');
    $requiredInputs.each(function() {
        if ($(this).val() != null || $(this).val() != undefined) {
            let len = $(this).val().length
            if (len <= 0) {
                valid = false
                $(this.id).get(0).setCustomValidity('This value is required.');
            }
        } else {
            valid = false;
            $(this.id).get(0).setCustomValidity('This value is required.');
        }
    });
    return valid;
}