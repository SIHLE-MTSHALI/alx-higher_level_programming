#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((result, current) => {
    result.push(current);
    return result;
  }, []);
};
