#!/usr/bin/node

const i = process.argv[2];
let j = 0;

if (parseInt(i)) {
  for (i; i > j; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
