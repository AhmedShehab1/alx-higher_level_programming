const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let count = 0;
  const jsonContent = JSON.parse(body);
  for (const result of jsonContent.results) {
    for (const character of result.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
