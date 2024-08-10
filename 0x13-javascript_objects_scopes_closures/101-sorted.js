#!/usr/bin/node
const dict = require('./101-data').dict;

const newObj = {};
for (const [no, id] of Object.entries(dict)) {
  if (id in newObj) {
    newObj[id].push(no);
  } else {
    newObj[id] = [no];
  }
}
console.log(newObj);
