#!/usr/bin/node
exports.addMeMaybe = function (number, theFuntion) {
  theFuntion(++number);
};
