var fs = require('fs');
var readMe = fs.readFileSync('./puzzle', 'utf8').split('\n');
readMe.forEach(function(x){
	readMe.forEach(function(y){
		readMe.forEach(function(z) {
			if(Number(x) + Number(y) + Number(z) == 2020){
			console.log(x*y*z);
			}
		})
	})
})