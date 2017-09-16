#!/usr/bin/node
let args = process.argv.slice(1);
let l = args.length;
let argsReturn = ['No argument', 'Argument found', 'Arguments found'];
if (l === 1) {
  console.log(argsReturn[0]);
} else if (l === 2) {
  console.log(argsReturn[1]);
} else {
  console.log(argsReturn[2]);
}
