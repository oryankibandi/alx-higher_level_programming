#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

try {
  request(url, (err, res, body) => {
    if (res) {
      console.log(`code: ${res.statusCode}`);
    }
  });
} catch (error) {
  console.log(error);
}
