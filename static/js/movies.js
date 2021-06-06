$("button[name=edit-movie]").on('click', function() {
  let id = $(this).data('movie-id');
  $("#edit_movie_id").val(id);
  $("#edit_movie").submit();
})

$("[name=review-btn], [name='edit-review-btn']").on("click", function() {
  $("#movie-review-modal").data("target-id", $(this).data("target-id"));
  $("#movie-review-modal textarea").val($(this).data("review"));
});

$("#movie-review-modal form").on("submit", function(e) {
  e.preventDefault();
  let review = $("#modal-review").val();
  let targetId = $("#movie-review-modal").data("target-id");

  const form = $("#" + targetId);
  form.find("[name=review]").val(review);
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