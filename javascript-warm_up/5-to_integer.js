#!/usr/bin/node

const arg = process.argv;
let num_check = Number.isInteger(arg);

if (num_check === true) {
  console.log("My number:" + arg[0]);
} else {
  console.log("Not a number");
}
