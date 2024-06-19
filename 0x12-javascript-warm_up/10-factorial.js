#!/usr/bin/node
function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return (1);
  }
  const result = a * factorial(a - 1);
  return (result);
}

console.log(factorial(parseInt(process.argv[2])));
