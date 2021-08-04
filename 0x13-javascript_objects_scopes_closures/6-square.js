#!/usr/bin/node

const SquareD = require('./5-square');

module.exports = class Square extends SquareD {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let rows = c;

    if (c === undefined) {
      c = 'X';
      rows = c;
    }
    for (let i = 0; i < this.size - 1; i++) {
      rows += c;
    }
    for (let j = 0; j < this.size; j++) {
      console.log(rows);
    }
  }
};
