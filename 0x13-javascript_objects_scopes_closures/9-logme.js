#!/usr/bin/node

let hello = 0;
exports.logMe = function (item) {
  console.log(`${hello}: ${item}`);
  hello++;
};
