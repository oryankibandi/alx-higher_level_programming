#!/usr/bin/node

const { writeFileSync } = require('node:fs');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];

try {
  request(url, (err, res, body) => {
    if (res) {
      try {
        writeFileSync(path, body, 'utf8');
      } catch (err) {
        console.log(err);
      }
    }
  });
} catch (error) {
  console.log(error);
}
