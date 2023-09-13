#!/usr/bin/node

const { argv } = require('process');
const x = argv[2];
if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < x; k++) {
    console.log('C is fun');
  }
}
