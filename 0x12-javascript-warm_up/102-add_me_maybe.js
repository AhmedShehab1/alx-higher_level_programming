#!/usr/bin/node
let y = 1;
let x;
exports.addMeMaybe = function (number, theFuntion) {
  if (y === 1) {
    x = number;
    y++;
  }
  theFuntion(++x);
};
