#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOcc = 0;

  list.forEach((e) => {
    if (e === searchElement) nbOcc += 1;
  });

  return (nbOcc);
};
