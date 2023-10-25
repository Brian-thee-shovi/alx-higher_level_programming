#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

request(myurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const done = {};
    const tasks = JSON.parse(body);
    for (const k in tasks) {
      const task = tasks[k];
      if (task.done === true) {
	if (done[task.userId] === undefined) {
          done[task.userId] = 1;
	} else {
	  done[task.userId]++;
	}
      }
    }
    console.log(done);
  } else {
    console.log('Error. Status code: ' + response.statusCode);
  }
});
