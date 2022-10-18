#!/usr/bin/node

const filename = process.argv[2];
const { readFileSync } = require("node:fs");

try {
  const content = readFileSync(filename, { encoding: "utf8" });
  console.log(content);
} catch (err) {
  console.log(err);
}
