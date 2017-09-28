$.get('https://swapi.co/api/films?format=json', function (data) {
  $.each(data.results, function (i, val) {
    $('ul#list_movies').append('<li>' + val.title + '</li>');
  });
});
