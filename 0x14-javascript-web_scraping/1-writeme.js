#!/usr/bin/node

const { writeFileSync } = require('node:fs');
const filename = process.argv[2];
const writable = process.argv[3];

try {
  writeFileSync(filename, writable, 'utf8');
} catch (err) {
  console.log(err);
}
