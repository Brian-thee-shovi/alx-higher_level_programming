#!/usr/bin/node

const { argv } = require('process');
const square = parseInt(argv[2]);
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(square));
