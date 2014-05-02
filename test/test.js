var tabdown = require('../');
var fs = require('fs');

fs.readFile('test/test.tabdown', function(err, data){
	if (err) throw err;
	var lines = data.toString().split('\n');
	console.log("\n> printing input:\n");
	console.log(lines);
	var tree = tabdown.parse(lines);
	console.log("\n> printing tree:\n");
	console.log(tree);

	console.log("\n> printing reconstructed:\n");
	tabdown.print(tree);
})
