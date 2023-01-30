#!/usr/bin/node

const arg = process.argv.slice(2);
const Num_check = Number.isInteger(arg);

if (Num_check === true) {
  console.log("My number:" + arg[0]);
} else {
  console.log("Not a number");
}
