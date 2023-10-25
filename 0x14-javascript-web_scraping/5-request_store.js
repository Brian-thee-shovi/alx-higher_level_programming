#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const myurl = process.argv[2];
const myfile = process.argv[3];

request(myurl, function (error, response, body) {
  if (!error) {
    fs.writeFile(myfile, body, 'utf8', function (error) {
      if (error) {
	console.log(error);
      }
    });
  }
});
