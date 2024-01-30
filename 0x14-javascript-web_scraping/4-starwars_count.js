#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('error:', error);
        return;
    }

    const films = JSON.parse(body).results;
    const wedgeAntillesID = '18';
    let count = 0;

    films.forEach(film => {
        if (film.characters.some(url => url.includes(`/people/${wedgeAntillesID}/`))) {
            count++;
        }
    });

    console.log(count);
});
