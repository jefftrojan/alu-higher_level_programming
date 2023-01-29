#!/usr/bin/node
const [argOne, argTwo] = process.argv.slice(2);
if (!argOne || !argTwo) {
  console.log('Two arguments are required');
} else {
  console.log(`${argOne} is ${argTwo}`);
}

