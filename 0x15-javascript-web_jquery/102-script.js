#!/usr/bin/node

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${lang}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
