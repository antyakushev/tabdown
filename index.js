exports.parse = function(lines, populate, marker) {
	var populate = populate || function(obj) { return obj;};
	var marker = marker || '\t';

	var TreeNode = function(data) {
		this.data = data;
		this.parent = null;
		this.children = [];
	}
	var tree = new TreeNode({
		'type': 'root',
	    	'depth': -1
	});
	var levels = [tree];

	for (var i = 0; i < lines.length; i++) {
		var line = lines[i];
		var hascontent = false;
		var tabcount = 0;


		for (var j = 0; j < line.length; j++) {
			var ch = line[j];;
			if ((ch == '\t')) {
				tabcount += 1;
			}else if (/[^\s]/.test(ch)){
				hascontent = true;
				break;
			}
		}
		if (hascontent) { //then add node to tree
			var content = {
				'line': line.substring(tabcount),
				'type': "line",
			};
			//populate later (with depth also)

			var node = new TreeNode(content);
			node.tabcount = tabcount;

			function topnode() {
		       		return levels[levels.length - 1];
			}
			while(node.tabcount - topnode().tabcount <= 0) {
				levels.pop();
			}
			node.data.depth = levels.length - 1;
			node = populate(node);
			node.parent = topnode();
			node.parent.children.push(node);
			levels.push(node);
		}
	}
	return tree;
}
exports.traverse = function (tree, cb){
	function _traverse(node) {
		cb(node);
		for (var i = 0; i < node.children.length; i++) {
			_traverse(node.children[i]);
		}
	}
	_traverse(tree);
}

exports.print = function(tree) {
	exports.traverse(tree, function(node) {
		if (node.data.type !== 'root') {
			var string = "";
			for (var i = 0; i < node.data.depth; i++) {
				string += "\t";
			}
			string += node.data.line;
			console.log(string);
		}
	});
}
