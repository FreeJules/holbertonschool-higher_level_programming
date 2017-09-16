#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
let args = process.argv.slice(1);
let a = parseInt(args[1]);
let b = parseInt(args[2]);
let sum = add(a, b);
console.log(sum);
