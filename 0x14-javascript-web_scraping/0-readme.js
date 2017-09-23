#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
let pathToFile = process.argv[2];

fs.readFile(pathToFile, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  } else {
    console.log(data);
  }
});
