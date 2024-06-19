#!/usr/bin/node
const sizeOfSquare = process.argv[2];
if (parseInt(sizeOfSquare)) {
  const x = parseInt(sizeOfSquare);
  let square = '';
  for (let i = 0; i < x; i++) {
    square += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
