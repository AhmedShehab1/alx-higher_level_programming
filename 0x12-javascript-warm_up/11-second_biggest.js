#!/usr/bin/node
const noArgs = process.argv.length;
if (noArgs <= 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  let secondMax = process.argv[2] - 1;

  for (let i = 3; i < process.argv.length; i++) {
    if (max < process.argv[i]) {
      max = process.argv[i];
    }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (max > process.argv[i] && secondMax < process.argv[i]) {
      secondMax = process.argv[i];
    }
  }

  console.log(secondMax);
}
