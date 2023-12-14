#!/usr/bin/node

const args = process.argv.slice(2);
const repetitions = parseInt(args[0], 10);

if (isNaN(repetitions)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < repetitions; i++) {
    console.log('C is fun');
  }
}
