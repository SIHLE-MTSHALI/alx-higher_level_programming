#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        acc += 1;
      }
      return acc;
    }, 0);
    console.log(count);
  } else {
    console.log(error);
  }
});
