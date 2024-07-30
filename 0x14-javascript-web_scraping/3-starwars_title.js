#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const jsonResponse = JSON.parse(response.body);
  console.log(jsonResponse.title);
});
