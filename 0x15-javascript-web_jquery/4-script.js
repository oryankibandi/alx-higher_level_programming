$(() => {
  const header = $("header");
  const red_header = $("#toggle_header");
  red_header.click(() => {
    header.attr("class", (idx, clss) => {
      return clss === "green" ? "red" : "green";
    });
  });
});
