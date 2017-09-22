#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
};
