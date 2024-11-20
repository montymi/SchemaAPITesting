const failedSchema = 'https://raw.githubusercontent.com/montymi/SchemaAPITesting/main/failed-schema.json';
const passedSchema = 'https://raw.githubusercontent.com/montymi/SchemaAPITesting/main/passed-schema.json';

function getRequest(schemaUrl) {
  return new Promise(function(resolve, reject) {
    pm.sendRequest({
      url: schemaUrl,
      method: 'GET',
      header: {
        'Content-Type': 'application/json',
      }
    }, function(err, res) {
      if (err) {
        reject(err);
      } else {
        resolve(res.json());
      }
    });
  });
}

getRequest(failedSchema)
  .then(function(response) {
    console.log(response);
    // Do something with the response here
    pm.test("Validate Schema", () => {
        pm.response.to.have.jsonSchema(response)
    });
  })
  .catch(function(error) {
    console.error(error);
  });

// getRequest(passedSchema)
//   .then(function(response) {
//     console.log(response);
//     pm.test("Validate Schema", () => {
//         pm.response.to.have.jsonSchema(response)
//     });
//   })
//   .catch(function(error) {
//     console.error(error);
//   });
