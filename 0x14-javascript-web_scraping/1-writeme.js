#!/usr/bin/node
// script that writes a string to a file
const fs = require('fs');
let pathToFile = process.argv[2];
let stringToWrite = process.argv[3];

fs.writeFile(pathToFile, stringToWrite, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
