#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

console.log(factorial(num));
