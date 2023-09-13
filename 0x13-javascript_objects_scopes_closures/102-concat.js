#!/usr/bin/node
const file1 = require('file1');
const n = file1.readFileSync(process.argv[2], 'utf8');
const k = file1.readFileSync(process.argv[3], 'utf8');
file1.writeFileSync(process.argv[4], n + k);
