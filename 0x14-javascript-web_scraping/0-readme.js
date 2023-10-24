#!/usr/bin/node
const my_file = process.argv[2];
const fs = require('fs');

fs.readFile(my_file, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
