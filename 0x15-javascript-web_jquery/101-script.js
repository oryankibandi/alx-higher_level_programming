$(document).ready(() => {
  const add = $("#add_item");
  const remove = $("#remove_item");
  const clear = $("#clear_list");
  const list = $(".my_list");
  const list_items = list.children();

  add.click(() => {
    list.append("<li>Item</li>");
  });

  remove.click(() => {
    list.children()[list.length - 1].remove();
  });

  clear.click(() => {
    list.children().remove();
  });
});
