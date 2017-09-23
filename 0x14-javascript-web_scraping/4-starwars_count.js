#!/usr/bin/node
// script that prints the number of movies where the character "Wedge Antilles" is present
let request = require('request');
let character = 'https://swapi.co/api/people/18/';
let requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let bodyJson = JSON.parse(body);
    let listOfFilms = bodyJson.results;
    let count = 0;
    for (let i = 0; i < listOfFilms.length; i++) {
      if (listOfFilms[i].characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
