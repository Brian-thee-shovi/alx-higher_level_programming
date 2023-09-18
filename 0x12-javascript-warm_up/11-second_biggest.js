#!/usr/bin/node

const my_args = process.argv.slice(2);
function findSecondBiggest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }
  numbers = numbers.map(Number);
  numbers.sort((a, b) => b - a);
  return numbers[1];
}
console.log(findSecondBiggest(my_args));
