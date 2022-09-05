#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num && typeof (num) === 'number') {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
