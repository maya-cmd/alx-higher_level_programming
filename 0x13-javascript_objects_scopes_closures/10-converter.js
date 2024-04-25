#!/usr/bin/node

exports.converter = function (base) {
  function numConverter (n) {
    return n.toString(base);
  }

  return numConverter;
};
