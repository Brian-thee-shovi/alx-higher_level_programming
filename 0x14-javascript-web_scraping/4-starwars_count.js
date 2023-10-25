#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

request(myurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const eachfilm in films) {
      const eachfilmchars = films[eachfilm].characters;
      for (const eachchar in eachfilmchars) {
	if (eachfilmchars[eachchar]. includes('18')) {
	  count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('Status code: ' + response.statusCode);
  }
});
