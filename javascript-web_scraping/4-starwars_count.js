#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charId = 18;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movies = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(`https://swapi-api.alx-tools.com/api/films/${charId}/`)) {
      count++;
    }
  }
  console.log(count);
});
