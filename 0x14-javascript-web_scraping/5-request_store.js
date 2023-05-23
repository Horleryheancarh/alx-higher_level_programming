#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
