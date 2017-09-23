#!/usr/bin/node
// script that computes the number of tasks completed by user id
let request = require('request');
let requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let jsonObj = {};
    for (let i = 1; i <= 10; i++) {
      jsonObj[i] = 0;
    }
    let bodyJson = JSON.parse(body);
    for (let j = 0; j < bodyJson.length; j++) {
      if (bodyJson[j].completed === true) {
        jsonObj[bodyJson[j].userId] += 1;
      }
    }
    console.log(jsonObj);
  }
});
