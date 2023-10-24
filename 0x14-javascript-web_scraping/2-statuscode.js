#!/usr/bin/node
const myquest = require('myquest');
const g = process.argv[2];

myquest(g, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
