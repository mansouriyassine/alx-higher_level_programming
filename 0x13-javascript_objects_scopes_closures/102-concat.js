#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./custom-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
  const data1 = fs.readFileSync(sourceFile1, 'utf8');
  const data2 = fs.readFileSync(sourceFile2, 'utf8');

  const concatenatedData = data1 + data2;

  fs.writeFileSync(destinationFile, concatenatedData, 'utf8');
  console.log(`Concatenated files ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
} catch (err) {
  console.error('An error occurred:', err.message);
  process.exit(1);
}
