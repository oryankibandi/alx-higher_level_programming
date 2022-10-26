$(() => {
  const character = $("#character");

  $.ajax({
    type: "GET",
    url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    success: (data) => {
      character.html(data.name);
    },
  });
});
