#!/usr/bin/node

const request = require('request');

function fetchCharacter(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                resolve(JSON.parse(body).name);
            }
        });
    });
}

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, async (error, response, body) => {
    if (error) {
        console.error('error:', error);
        return;
    }

    const film = JSON.parse(body);
    for (const characterUrl of film.characters) {
        try {
            const name = await fetchCharacter(characterUrl);
            console.log(name);
        } catch (error) {
            console.error('error:', error);
        }
    }
});
