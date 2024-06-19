#!/usr/bin/node
const noOfArguments = process.argv.length;
if (noOfArguments === 2) {
  console.log('No argument');
} else if (noOfArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
