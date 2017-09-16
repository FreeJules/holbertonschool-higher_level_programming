#!/usr/bin/node
let args = process.argv.slice(1);
let length = args.length;
if (length < 3) {
  console.log('0');
} else {
  args = args.sort(function (a, b) { return a - b; });
  console.log(args[length - 2]);
}
