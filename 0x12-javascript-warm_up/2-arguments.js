#!/usr/bin/node

const { argv } = require('process');
//func is used to import built-in process module in node.js
//argv is destructures from the imported process
//curly braces are part of destructuring syntax
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
