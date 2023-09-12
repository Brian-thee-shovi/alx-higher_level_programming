#!/usr/bin/node

exports.esrever = function (list) {
  const list_reverse = [];
  for (let k = list.length - 1; k >= 0; k--) {
    list_reverse.push(list[k]);
  }
  return list_reverse;
};
