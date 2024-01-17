#!/usr/bin/node
// defines a script that prints all
// characters of a Star Wars movie


const request = require('request');


function getCharaters(movieId) {
  const baseUrl = 'https://swapi.dev/api/';
  const filmUrl = `${baseUrl}films/${movieId}/`;
  request.get(filmUrl, (error, reponse, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const filmData = JSON.parse(body);
    if (filmData.detail && filmData.detail === 'Not found') {
      console.log(`Movie with ID ${movieId} not found.`);
      return;
    }
    const charactersUrls = filmData.characters;
    const fetchCharater = (index) => {
      if (index >= charactersUrls.length) {
        return;
      }
      request.get(charactersUrls[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
	  return;
        }
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
        fetchCharacter(index + 1);
      });
    };
  });
}

if (process.argv.length !== 2) {
  console.log('Usage: ./script.js <movie_id>')
  process.exit(1)
}
const movieId = process.argv[2];

try {
  const movieIdInt = parseInt(movieId, 10);
  if (isNaN(movieIdInt)) {
    console.log('Movie ID must be an integer.');
    process.exit(1);
  }

  getCharacters(movieIdInt);
} catch (error) {
    console.error('Error:', error.message || error);
}
