const first_arg = process.argv[2];
if (parseInt(first_arg))
{
	console.log(`My number: ${parseInt(first_arg)}`);
}
else
{
	console.log("Not a number");
}
