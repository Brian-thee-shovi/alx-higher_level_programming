#!/usr/bin/node
const myfile = process.argv[2];
const strng = process.argv[3];
const fs = require('fs');

fs.writeFile(myfile, strng, 'utf8', fuction (err) {
  if (err) {
    console.log(err);
  }
});
