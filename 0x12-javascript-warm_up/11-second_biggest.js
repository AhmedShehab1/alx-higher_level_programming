#!/usr/bin/node
noArg = process.argv.length;
if (noArg <= 3) {
	console.log(0);
}
else {
	let max = process.argv[2];
	let secondMax = process.argv[2];
	for (let i = 3; i < noArg; i++) {
		if (max < process.argv[i]) {
			max = process.argv[i];
		}
		if (process.argv[i] > secondMax && process.argv[i] < max + 1) {
			secondMax = process.argv[i];
		}
	}
	console.log(secondMax);
}
