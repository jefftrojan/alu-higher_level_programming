#!/usr/bin/node
exports.repeat = function (x, theFunction) {
  while (x > 0) {
    theFunction.call();
    x--;
  }
};
