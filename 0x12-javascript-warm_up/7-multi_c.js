#!/usr/bin/node
let args = process.argv.slice(1);
let errorMsg = 'Missing number of occurrences';
let check = Number(args[1]);
if (!check) {
  console.log(errorMsg);
} else {
  let x = parseInt(check);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
