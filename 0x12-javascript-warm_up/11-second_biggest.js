#!/usr/bin/node

let big = 0;
let secBig = 0;

for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > big) {
    big = parseInt(process.argv[i]);
  }
  if (parseInt(process.argv[i]) > secBig && parseInt(process.argv[i]) < big) {
    secBig = parseInt(process.argv[i]);
  }
}

console.log(secBig);
