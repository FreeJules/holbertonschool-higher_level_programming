$(document).ready(function () {
  $('INPUT#btn_search').click(function () {
    // Get
    let city = $('INPUT#city_search').val();
    // Set
    $('INPUT#city_search').val(city);
    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json', function (data) {
      $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
    });
  });
});
