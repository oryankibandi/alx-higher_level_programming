#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

const getCharacterNames = async (urls) => {
  const len = urls.length;

  for (let i = 0; i < len; i++) {
    try {
      console.log('i:', i);
      request(urls[i], (err, res, body) => {
        console.log('querying: ', urls[i]);
        console.log(JSON.parse(body).name);
      });
    } catch (error) {
      console.log(error);
    }
  }
};

request(url, async (err, res, body) => {
  try {
    const charactersUrl = JSON.parse(body).characters;
    await getCharacterNames(charactersUrl);
  } catch (error) {
    console.log(error);
  }
});
