#!/usr/bin/node

const { argv } = require('process');
const square = parseInt(argv[2]);
if (isNaN(square) === true) {
  console.log('Missing size');
} else {
  for (let k = 0; k < square; k++) {
    let row = '';
    for (let b = 0; b < square; b++) {
      row += 'X';
    }
    console.log(row);
  }
}
