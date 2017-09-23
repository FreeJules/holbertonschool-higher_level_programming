#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
let request = require('request');
const fs = require('fs');
let requestURL = process.argv[2];
let pathToFile = process.argv[3];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(pathToFile, body, 'utf8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
