#!/usr/bin/node
const _Square_ = require('./5-square');

class Square extends _Square_ {
  charPrint (c) {
    if (c) {
      let rectangle = '';
      for (let i = 0; i < this.width; i++) {
        rectangle += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(rectangle);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
