#!/usr/bin/node
// prints all characters of a Star Wars movie
let request = require('request');
let requestURL = 'https://swapi.co/api/films/' + process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let bodyJson = JSON.parse(body);
    let characterLinks = bodyJson.characters;
    for (let i = 0; i < characterLinks.length; i++) {
      request(characterLinks[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          let name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
