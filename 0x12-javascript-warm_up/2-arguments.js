#!/usr/bin/node
const no_of_arguments = process.argv.length;
if (no_of_arguments == 2) {
	console.log("No argument");
}
else if (no_of_arguments == 3) {
	console.log("Argument found");
}
else {
	console.log("Arguments found");
}
