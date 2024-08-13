#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destFile = process.argv[4];

fs.readFile(file1, 'utf-8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(file2, 'utf-8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }
    const data = data1 + data2;
    fs.writeFile(destFile, data, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
