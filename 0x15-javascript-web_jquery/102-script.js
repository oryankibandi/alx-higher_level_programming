$(document).ready(() => {
  const lang_code = $("#language_code");
  const button = $("#btn_translate");

  button.click(() => {
    $.ajax({
      type: "GET",
      url: "https://stefanbohacek.com/hellosalut/?lang=" + lang_code.val(),
      success: (data) => {
        $("#hello").html(data.hello);
      },
    });
  });
});
