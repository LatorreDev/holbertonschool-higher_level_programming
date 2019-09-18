#!/usr/bin/node
let i;
const size = process.argv[2];

if (parseInt(size)) {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
