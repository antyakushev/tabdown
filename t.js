/*
 * t - a todolist parser
 */

var fs = require('fs');
var clc = require('cli-color');

var filename = "s"
process.chdir(process.env.HOME);



var file = fs.readFileSync(filename);
var keyword = "#Today\n"
var lines = file.toString().split(keyword);
lines = lines[lines.length-1].split(/\n/);

var tasks = [];
var counter = -1;
while(lines.length > 0){
	var line = lines.shift();
	if( /^\t[0-9]/.test(line)){
		counter++;
		var priority = line[1];
		tasks[counter] = [priority, line.substring(3)]
	}else{
		if(line !== ""){
			tasks[counter].push(line.substring(1));
		}
	}
}
tasks.sort(function(a,b){
	return b[0] - a[0];
});
var print = function(task){
	var priority = task.shift();
	var color = [clc.cyan,clc.red,clc.green, clc.blue];
	if(priority in color){
		while(task.length > 0){
			console.log('\t' + color[priority](task.shift()));
		}
		console.log();
	}
}
if (process.argv[2] === '--now'){
	console.log(tasks[tasks.length-1][1]);
}else{
	for(t in tasks){
		print(tasks[t]);
	}
}
	
