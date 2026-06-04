#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(n => parseInt(n));

  let max = -Infinity;
  let second = -Infinity;

  for (const n of nums) {
    if (n > max) {
      second = max;
      max = n;
    } else if (n > second && n < max) {
      second = n;
    }
  }

  console.log(second);
}