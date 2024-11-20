// postmanTestingV2.js - runs within Postman
const failedSchema = 'https://raw.githubusercontent.com/montymi/SchemaAPITesting/main/failed-schema.json'; 
const passedSchema = 'https://raw.githubusercontent.com/montymi/SchemaAPITesting/main/passed-schema.json';


const fetchSchema = async (schemaUrl) => {
    // Function to fetch schema from url
    try {
        const response = await pm.sendRequest({
            url: schemaUrl,
            method: 'GET',
            header: {
                'Content-Type': 'application/json',
            },
        });

        if (response.status !== 200) {
            throw new Error(`Failed to fetch schema: ${response.status} ${response.statusText}`);
        }

        return response.json(); // `await` not needed in Postman here!
    } catch (error) {
        console.error('Error fetching schema:', error.message);
        throw error;
    }
};

const validateSchema = async (schemaUrl) => {
    // Function to validate schema from url
    try {
        const schema = await fetchSchema(schemaUrl);
        console.log('Schema fetched successfully:', schema);

        pm.test('Validate Schema', () => {
            pm.response.to.have.jsonSchema(schema);
        });

    } catch (error) {
        console.error('Schema validation failed:', error.message);
    }
};

// EXECUTE VALIDATION TESTING

validateSchema(failedSchema);
// validateSchema(passedSchema);
