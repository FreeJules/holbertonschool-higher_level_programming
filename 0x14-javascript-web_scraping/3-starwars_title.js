#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
let request = require('request');
let episodeNumber = process.argv[2];
let requestURL = 'http://swapi.co/api/films/' + episodeNumber;
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let bodyJson = JSON.parse(body);
    console.log(bodyJson['title']);
  }
});
