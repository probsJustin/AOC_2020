var fs = require('fs');
var readMe = fs.readFileSync('./puzzle', 'utf8').split('\n');
readMe.forEach(function(x){
	readMe.forEach(function(Number(y)){
		if(Number(x) + Number(y) == 2020){
		console.log(x*y);
		}
	})
})

