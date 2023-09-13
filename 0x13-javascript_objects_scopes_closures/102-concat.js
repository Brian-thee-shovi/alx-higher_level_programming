#!/usr/bin/node
const file = require('file');
const n = file.readFileSync(process.argv[2], 'utf8');
const k = file.readFileSync(process.argv[3], 'utf8');
file.writeFileSync(process.argv[4], n + k);
