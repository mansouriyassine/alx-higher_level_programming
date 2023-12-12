#!/usr/bin/node

const fs = require('fs');

const [,, sourceFile1, sourceFile2, destinationFile] = process.argv;

const src1 = fs.readFileSync(sourceFile1, 'utf8');
const src2 = fs.readFileSync(sourceFile2, 'utf8');
fs.writeFileSync(destinationFile, src1 + src2);
