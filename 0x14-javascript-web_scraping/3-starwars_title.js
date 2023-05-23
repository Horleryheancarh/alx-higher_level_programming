#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + id, function (err, res, body) {
  if (err == null) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  } else {
    console.log(err);
  }
});
