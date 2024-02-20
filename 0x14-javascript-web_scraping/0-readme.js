#!/usr/bin/node
//read from a file

const file = require('fs')
file.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
       return;
    }
    console.log(data);
  });
