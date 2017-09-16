#!/usr/bin/node
let args = process.argv.slice(1);
if (args[1]) {
  console.log(args[1]);
} else {
  console.log('No argument');
}
