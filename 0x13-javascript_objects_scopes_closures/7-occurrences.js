#!/usr/bin/node
/**
 * Function reeturns numbeer of occurences n a list
 *
 */
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let i = 0; i < list.length; i++) {
    counter = (list[i] === searchElement ? counter + 1 : counter);
  }

  return counter;
};
