#!/usr/bin/node

const m = process.argv.slice(2);
function findSecondBiggest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }
  numbers = numbers.map(Number);
  numbers.sort((a, b) => b - a);
  return numbers[1];
}
console.log(findSecondBiggest(m));
