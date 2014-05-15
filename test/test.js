var tabdown = require('../');
var fs = require('fs');

fs.readFile('test/list.td', function(err, data){
	if (err) throw err;
	var lines = data.toString().split('\n');
	console.log("\n> printing input:\n");
	console.log(lines);
	var tree = tabdown.parse(lines);
	console.log("\n> printing tree:\n");
	console.log(tree); //Node and Chromium use the original toString for console.log
	console.log("\n> printing stringified tree:\n");
	console.log(tree.toString());
	console.log("\n> printing reconstructed:\n");
	tabdown.print(tree);
	
	console.log("\n> traversing and printing:\n");
	tabdown.traverse(tree, function(node) {console.log(node.depth, node.data)});

	console.log("\n> json:\n");
	console.log(tabdown.toJSON(tree));
})
