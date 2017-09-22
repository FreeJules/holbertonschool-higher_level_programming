#!/usr/bin/node
// Class Rectangle that defines a rectangle
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && w && h > 0 && h) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      let recStr = '';
      for (let j = 0; j < this.width; j++) {
        recStr += 'X';
      }
      console.log(recStr);
    }
  };
};
