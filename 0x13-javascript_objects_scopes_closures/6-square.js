#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js
exports.Square = Square;

const newSquare = require('./5-square').Square;

function Square (size) {
  newSquare.call(this, size);
}

Square.prototype.charPrint = function (c = 'X') {
  // refactor print in Rectangle to take param so that it can be called here
  for (let i = 0; i < this.width; i++) {
    let s = '';
    for (let j = 0; j < this.height; j++) {
      s += c;
    }
    console.log(s);
  }
};
