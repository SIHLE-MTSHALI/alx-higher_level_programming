#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (err, res, characterBody) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(characterBody).name);
        }
      });
    });
  } else {
    console.log(error);
  }
});
