#!/usr/bin/node

function factorial (n) {
  if (n < 0 || n === 0) {
    return;
  }
  return n * factorial(n - 1);
}

factorial(parseInt(process.argv[2]));
