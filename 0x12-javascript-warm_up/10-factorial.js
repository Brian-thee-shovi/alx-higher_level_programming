#!/usr/bin/node

const { argv } = require('process');
const square = parseInt(argv[2]);
function factorial (d) {
  if (isNaN(d)) {
    return 1;
  } else if (d === 0 || d === 1) {
    return 1;
  } else {
    return d * factorial(d - 1);
  }
}
consolle.log(factorial(square));
