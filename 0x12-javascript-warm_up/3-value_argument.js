#!/usr/bin/node
const commandLineArguments = process.argv;

if (commandLineArguments.length <= 2) {
  console.log('No argument');
} else {
  console.log(commandLineArguments[2]);
}
