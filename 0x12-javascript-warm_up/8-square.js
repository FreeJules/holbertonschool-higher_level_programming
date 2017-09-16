#!/usr/bin/node
let args = process.argv.slice(1);
let errorMsg = 'Missing size';
let square = '';
let check = Number(args[1]);
if (!check) {
  console.log(errorMsg);
} else {
  let x = parseInt(check);
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    square += '\n';
  }
  square = square.slice(0, -1);
  console.log(square);
}
