#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function getMovieCharacters (movieId) {
  try {
    const filmData = await fetchData(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const characters = filmData.characters || [];

    for (const characterUrl of characters) {
      const characterData = await fetchData(characterUrl);
      console.log(characterData.name || 'Unknown');
    }
  } catch (error) {
    console.error(error);
  }
}

getMovieCharacters(movieId);
