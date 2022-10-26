$(() => {
  const list = $(".my_list");
  const add = $("#add_item");
  add.click(() => {
    list.append("<li>Item</li>");
  });
});
