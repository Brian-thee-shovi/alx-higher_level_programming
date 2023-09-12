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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
