#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

if (args.length < 2) {
  console.log(NaN);
} else {
  console.log(add(parseInt(args[0], 10), parseInt(args[1], 10)));
}
