#imported json module
import json
#imported internal python module
import sys
# Read the schema file name from the command line argument
#if length of the argument in the command line is less then 2 it shows the print statement
if len(sys.argv) < 2:
    print("Python Program file and schema file name should be included in the command line argument in the terminal Ex: GenerateInstanceSchema.py <NameofSchemafile>")
    exit()
    #Displays the command line arguments by extracting all the elements that is contained in the input file
DB_schema_path = sys.argv[1]

# Load the database schema from the input file
DB_schema_path = '/Users/euniceolorunshola/Desktop/Database and the Web/Project3/Part2/StudentDBSchema.json'
with open(DB_schema_path) as f:
        #convert from json to python by parsing the json string from the filepath of the input file
 DB_schema_path = json.load(f)

# Create a new schema instances for the database input file
generate_instance_schema = {
"$schema":  "http://json-schema.org/draft-07/schema#",
"description": "This is the generated instance schema for inputted database schema file",
"type" : "object",
"properties":{}
}
# Loop over each entity in the instance schema
for entity in DB_schema_path["entities"]:
    instance_schema_entity_name = entity["name"]
    instance_schema_entity_attributes = entity['attributes']
    
    # Define the properties for the entity in the instance schema
    properties = {}
    # Loop over each attribute in the entity
    for attribute in instance_schema_entity_attributes:
        properties[attribute['name']] = {"type": attribute['type']}
        if attribute['type'] == "integer":
            properties[attribute['name']]["minimum"] = 0
        if attribute['type'] == "string":
            properties[attribute['name']]["maxLength"] = attribute['size']
    # Add the properties for the entity in the instance schema
    generate_instance_schema['properties'][instance_schema_entity_name] = {
        "type": "object",
        "properties": properties,
        "required": [attribute['name'] for attribute in instance_schema_entity_attributes if attribute['name'] in entity['primaryKey']]
    }

# Print the instance schema as a JSON string to the terminal
print(json.dumps(generate_instance_schema, indent=4))