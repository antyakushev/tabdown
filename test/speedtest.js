var tabdown = require('../');
var fs = require('fs');

fs.readFile('test/biglist.td', function(err, data){
	if (err) throw err;
	var lines = data.toString().split('\n');
	var start = new Date();
	for (var i = 0; i < 1000; i++) {
    	tabdown.parse(lines);
    }	
	var time = new Date() - start;
	console.log("\n> Parsing took", time, "ms");
})
