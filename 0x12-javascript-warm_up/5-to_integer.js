#!/usr/bin/node
let args = process.argv.slice(1);
let arg = Number(args[1]);
if (!arg) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg));
}
