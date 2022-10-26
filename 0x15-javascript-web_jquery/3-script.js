$(() => {
  const header = $("header");
  const red_header = $("#red_header");
  red_header.click(() => {
    header.attr("class", "red");
  });
});
