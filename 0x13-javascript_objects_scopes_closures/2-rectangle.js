#!/usr/bin/node
// Class Rectangle that defines a rectangle
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && w && h > 0 && h) {
    this.width = w;
    this.height = h;
  }
};
