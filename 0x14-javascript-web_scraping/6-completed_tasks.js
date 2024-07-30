#!/usr/bin/node
const request = require('request');

const result = {};
request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  for (const obj of JSON.parse(body)) {
    if (obj.userId in result && obj.completed) {
      result[obj.userId] += 1;
    } else if (obj.completed) {
      result[obj.userId] = 1;
    }
  }
  console.log(result);
});
