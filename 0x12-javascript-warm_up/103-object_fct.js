#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function increament(obj) {
  obj.value += 1;
}

myObject.incr = increament;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
