#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0; i < list.length / 2; i++) {
    const temp = list[j];
    list[j] = list[i];
    list[i] = temp;
    j--;
  }
  return (list);
};
