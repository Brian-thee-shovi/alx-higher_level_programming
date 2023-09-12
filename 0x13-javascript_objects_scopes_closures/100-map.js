#!/usr/bin/node

const mylist = require('./100-data').mylist;
const myarray = mylist.map((b, n) => b * n);

console.log(mylist);
console.log(myarray);
