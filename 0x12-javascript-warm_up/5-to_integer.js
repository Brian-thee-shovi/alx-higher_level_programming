#!/usr/bin/node

const { argv } = require('process');
const int_v = parseInt(argv[2]);

if (isNaN(int_v) === false) {
  console.log('My number: ' + int_v);
} else {
  console.log('Not a number');
}
