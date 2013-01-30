#!/usr/bin/env node

var fs = require('fs');
var clc = require('cli-color');

var filename = "s"
var keyword = "#Today\n"
process.chdir(process.env.HOME);



fs.readFile(filename,function(err,data){
	var input = data.toString().split(keyword);
	input = input[input.length-1].split(/\n/);
	var lines = []
	for( a in input){
		if(input[a] !== ""){
			lines.push(input[a]);
		}
	}

	var tasks = [];
	var counter = -1;
	while(lines.length > 0){
		var line = lines.shift();
		if( /^\t[0-9]/.test(line)){
			counter++;
			var priority = line[1];
			tasks[counter] = [priority, line.substring(3)]
		}else{
			tasks[counter].push(line.substring(1));
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
	if(process.argv[2] === '--now'){
		console.log(tasks[tasks.length-1][1]);
	}else{
		for(t in tasks){
			print(tasks[t]);
		}
	}
	
});
