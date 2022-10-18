#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const countAppearances = (results) => {
  let app = 0;

  try {
    results.forEach((item) => {
      if (
        item.characters.includes('https://swapi-api.hbtn.io/api/people/18/')
      ) {
        app++;
      }
    });

    console.log(app);
  } catch (error) {
    console.log(error);
  }
};

request(url, (err, res, body) => {
  try {
    if (body) {
      const data = JSON.parse(body);

      countAppearances(data.results);
    }
  } catch (error) {
    console.log(error);
  }
});
