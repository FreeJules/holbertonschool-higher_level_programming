#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}
let args = process.argv.slice(1);
let num = 0;
if (Number(args[1])) {
  num = parseInt(Number(args[1]));
}
console.log(factorial(num));
