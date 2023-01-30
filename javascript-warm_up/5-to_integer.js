#!/usr/bin/node

const arg = process.argv[2];
const Numcheck = Number.isInteger(arg);

if (!Numcheck === true) {
  console.log(`My number: ${arg}`);
}

if (!Numcheck === false) {
  console.log('Not a number');
}
