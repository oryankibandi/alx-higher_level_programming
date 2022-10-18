#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const completed = {};

const countCompleted = (data) => {
  data.forEach((todo) => {
    if (todo.completed === true) {
      if (completed[`${todo.userId}`]) {
        completed[`${todo.userId}`] = completed[`${todo.userId}`] + 1;
      } else {
        completed[`${todo.userId}`] = 1;
      }
    }
  });
};

try {
  request(url, (err, res, body) => {
    countCompleted(JSON.parse(body));
    console.log(completed);
  });
} catch (error) {
  console.log(error);
}
