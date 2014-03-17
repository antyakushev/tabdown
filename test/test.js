var tabdown = require('./');
var fs = require('fs');

fs.readFile('/home/slee2/s', function(err, data){
	var lines = data.toString().split('\n');
	var tree = tabdown.parse(lines);
	tabdown.print(tree);
})
