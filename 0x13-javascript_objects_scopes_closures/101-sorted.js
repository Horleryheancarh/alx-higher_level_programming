#!/usr/bin/node
const dict = require('./101-data').dict;
const nDict = {};

Object.keys(dict).map(function (key, index) {
  if (nDict[dict[key]] === undefined) {
    nDict[dict[key]] = [];
  }
  nDict[dict[key]].push(key);
});

console.log(nDict);
