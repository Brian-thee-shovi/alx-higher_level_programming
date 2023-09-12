#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let k = 0; k < this.height; k++) {
      let row = '';
      for (let b = 0; b < this.width; b++) {
	row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;

