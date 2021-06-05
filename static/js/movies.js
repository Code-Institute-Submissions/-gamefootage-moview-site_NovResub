$("button[name=edit-movie]").on('click', function() {
  let id = $(this).data('movie-id');
  $("#edit_movie_id").val(id);
  $("#edit_movie").submit();
})