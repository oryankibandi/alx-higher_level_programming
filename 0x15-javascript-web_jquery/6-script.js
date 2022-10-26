$(() => {
  const header = $("header");
  const update = $("#update_header");
  update.click(() => {
    header.html("New Header!!!");
  });
});
