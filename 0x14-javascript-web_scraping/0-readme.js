#!/usr/bin/node
const myfile = process.argv[2];
const fs = require('fs');

fs.readFile(myfile, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
