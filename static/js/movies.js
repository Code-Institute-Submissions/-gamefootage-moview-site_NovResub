$("button[name=edit-movie]").on('click', function() {
  let id = $(this).data('movie-id');
  $("#edit_movie_id").val(id);
  $("#edit_movie").submit();
})

$("[name=review-btn]").on("click", function() {
  $("#movie-review-modal").data("movie-id", $(this).data("movie-id"));
});

$("#movie-review-modal form").on("submit", function(e) {
  e.preventDefault();
  let review = $("#modal-review").val();
  let movieId = $("#movie-review-modal").data("movie-id");

  const form = $("form[data-movie-id=" + movieId + "]");
  form.find("[name=review]").val(review);
  form.submit();
});