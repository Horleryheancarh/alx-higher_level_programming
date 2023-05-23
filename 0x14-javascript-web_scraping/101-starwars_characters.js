#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
let id = parseInt(process.argv[2]);
let characters = [];

request(apiUrl, function (err, res, body) {
  if (err == null) {
    const obj = JSON.parse(body);
    const results = obj.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === id) {
        characters = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], function (err, res, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log(err);
  }
});
