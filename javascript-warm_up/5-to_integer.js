#!/usr/bin/node

const arg = process.argv.slice(2);
const Numcheck = Number.isInteger(arg);

if (!Numcheck === true) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
