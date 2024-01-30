#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesID = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(wedgeAntillesID)) {
      count++;
    }
  });

  console.log(count);
});
