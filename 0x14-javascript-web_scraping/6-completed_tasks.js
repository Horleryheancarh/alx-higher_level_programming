#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err == null) {
    const data = {};
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed === true) {
        if (data[obj[i].userId] === undefined) {
          data[obj[i].userId] = 0;
        }
        data[obj[i].userId]++;
      }
    }
    console.log(data);
  }
});
