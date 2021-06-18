$(document).ready(function() {
  if ( $("#user-check").val() !== "true" ) {
    const instance = M.Modal.getInstance($("#login-modal"));
    instance.open();
  }

  // StackOverflow rating input 
  // (https://stackoverflow.com/questions/8118266/integrating-css-star-rating-into-an-html-form)
  $(".rating input:radio").attr("checked", false);

  $('.rating input').click(function () {
    $(".rating span").removeClass('checked');
    $(this).parent().addClass('checked');
  });
});

$("button[name=edit-movie]").on('click', function() {
  let id = $(this).data('movie-id');
  $("#edit_movie_id").val(id);
  $("#edit_movie").submit();
});

$("[name=review-btn], [name='edit-review-btn']").on("click", function() {
  $("#movie-review-modal").data("target-id", $(this).data("target-id"));
  $("#movie-review-modal textarea").val($(this).data("review"));
  
  if (parseInt($(this).data("rating")) > 0 && parseInt($(this).data("rating")) < 6)
    $("#movie-review-modal input[value=" + $(this).data("rating") + "]").click();
});

$("#movie-review-modal form").on("submit", function(e) {
  e.preventDefault();
  let review = $("#modal-review").val();
  let rating = $("#movie-review-modal input:radio:checked").val();
  let targetId = $("#movie-review-modal").data("target-id");

  const form = $("#" + targetId);
  form.find("[name=review]").val(review);
  form.find("[name=rating]").val(rating);
  form.submit();
});

$("[name='delete-review-btn']").on("click", function() {
  $("#confirm-modal").data("target-id", $(this).data("target-id"));
  $("#confirm-modal").find(".confirmation-message").text($(this).data("message"));
});

$("#confirm-modal form").on("submit", function(e) {
  e.preventDefault();
  let targetId = $("#confirm-modal").data("target-id");
  const form = $("#" + targetId);
  form.submit();
})