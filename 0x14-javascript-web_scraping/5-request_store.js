#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const myurl = process.argv[2];
const myfile = process.argv[3];

request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(file, body, 'utf8', function (error) {
      if (error) {
	console.log(error);
      }
    });
  }
});
