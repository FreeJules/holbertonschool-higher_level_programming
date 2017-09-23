#!/usr/bin/node
// script that computes the number of tasks completed by user id
let request = require('request');
let requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let jsonObj = {};
    let bodyJson = JSON.parse(body);
    for (let j = 0; j < bodyJson.length; j++) {
      if (bodyJson[j].completed === true) {
        let uid = bodyJson[j].userId;
        if (jsonObj.hasOwnProperty(uid)) {
          jsonObj[uid] += 1;
        } else {
          jsonObj[uid] = 1;
        }
      }
    }
    console.log(jsonObj);
  }
});
