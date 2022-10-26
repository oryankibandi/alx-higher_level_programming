$(document).ready(() => {
  const lang_code = $("#language_code");
  const button = $("#btn_translate");

  const translate = () => {
    $.ajax({
      type: "GET",
      url: "https://stefanbohacek.com/hellosalut/?lang=" + lang_code.val(),
      success: (data) => {
        $("#hello").html(data.hello);
      },
    });
  };

  button.click(() => {
    translate();
  });

  lang_code.keydown((event) => {
    key = event.keyCode ? event.keyCode : event.which;
    if (key == 13) {
      translate();
    }
  });
});
