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

async function main() {
  const movieID = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

  request(url, async (error, response, body) => {
    if (error) {
      console.error('error:', error);
      return;
    }

    const film = JSON.parse(body);
    const characterPromises = film.characters.map(fetchCharacter);

    try {
      const characters = await Promise.all(characterPromises);
      characters.forEach(character => console.log(character));
    } catch (error) {
      console.error('error:', error);
    }
  });
}
