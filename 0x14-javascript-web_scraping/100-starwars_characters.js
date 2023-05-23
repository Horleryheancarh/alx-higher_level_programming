#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, function (err, res, body) {
  if (err == null) {
    const obj = JSON.parse(body);
    const characters = obj.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, res, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
