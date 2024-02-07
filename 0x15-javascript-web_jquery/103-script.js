#!/usr/bin/node

$(document).ready(function () {
  function getTranslation() {
    const lang = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${lang}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(getTranslation);
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      getTranslation();
    }
  });
});
