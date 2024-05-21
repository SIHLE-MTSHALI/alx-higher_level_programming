#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];

request(API_URL, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const films = JSON.parse(body).results;
        const wedgeAntillesId = 18; 

        const count = films.reduce((total, film) => {
            return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`) 
                ? total + 1 
                : total;
        }, 0);

        console.log(count);
    }
});
