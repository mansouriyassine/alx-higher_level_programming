#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  let max = -Infinity; let secondMax = -Infinity;

  args.forEach(num => {
    const number = parseInt(num, 10);
    if (number > max) {
      secondMax = max;
      max = number;
    } else if (number > secondMax && number !== max) {
      secondMax = number;
    }
  });

  return secondMax;
}

const args = process.argv.slice(2);
console.log(findSecondBiggest(args));
