$(() => {
  const movies = $("#list_movies");

  $.ajax({
    type: "GET",
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    success: (data) => {
      $.each(data.results, (i, result) => {
        movies.append("<li>" + result.title + "</li>");
      });
    },
  });
});
