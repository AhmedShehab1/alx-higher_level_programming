$('#toggle_header').on('click', function () {
  $(this).attr('class', function (i, currCls) {
    return currCls === 'red' ? 'green' : 'red';
  });
});
