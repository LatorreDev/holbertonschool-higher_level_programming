#!/usr/bin/node
// Define a rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    let i = 0;
    for (i; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
