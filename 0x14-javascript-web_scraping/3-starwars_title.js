#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

try {
  request(url, (err, res, body) => {
    if (body) {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
} catch (error) {
  console.log(error);
}
