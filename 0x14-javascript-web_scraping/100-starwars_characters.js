#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

const getCharacterNames = (urls) => {
  try {
    urls.forEach((url) => {
      request(url, (err, res, body) => {
        console.log(JSON.parse(body).name);
      });
    });
  } catch (error) {
    console.log(error);
  }
};

request(url, (err, res, body) => {
  try {
    const charactersUrl = JSON.parse(body).characters;
    getCharacterNames(charactersUrl);
  } catch (error) {
    console.log(error);
  }
});
