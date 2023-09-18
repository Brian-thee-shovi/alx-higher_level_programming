#!/usr/bin/node

function callme (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
}
module.exports = {
  callme
};
