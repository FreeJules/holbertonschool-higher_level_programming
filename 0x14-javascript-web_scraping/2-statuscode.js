#!/usr/bin/node
// script that display the status code of a GET request
let request = require('request');
let requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
