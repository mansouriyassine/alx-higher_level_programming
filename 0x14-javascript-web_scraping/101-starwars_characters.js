#!/usr/bin/node

const request = require('request');

function fetchCharacters(movieID) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;
  
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const film = JSON.parse(body);
        const characters = film.characters;
        resolve(characters);
      }
    });
  });
}

async function printCharacterNames(movieID) {
  try {
    const characterUrls = await fetchCharacters(movieID);
    
    for (const url of characterUrls) {
      const character = await fetchCharacter(url);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

async function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character);
      }
    });
  });
}

const movieID = process.argv[2];

if (!movieID) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
} else {
  printCharacterNames(movieID);
}


main();
