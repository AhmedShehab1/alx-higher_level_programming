$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  for (const result of data.results) {
    $(`<li>${result.title}</li>`).appendTo('#list_movies');
  }
});
