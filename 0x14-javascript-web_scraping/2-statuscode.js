#!/usr/bin/node
const myquest = require('myquest');
const url = process.argv[2];

myquest(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
