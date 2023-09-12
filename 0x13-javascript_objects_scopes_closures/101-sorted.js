#!/usr/bin/node

const { dict } = require('./101-data');

const my_v = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});
console.log(my_v);
