#imported json module
import json
#imported internal python module
import sys
# Read the schema file name from the command line argument
#if length of the argument in the command line is less then 2 it shows the print statement
if len(sys.argv) < 2:
    print("Python Program file and schema file name should be included in the command line argument in the terminal Ex: GenerateRelationalDesign.py <NameofSchemafile>")
    exit()
    #Displays the command line arguments by extracting all the elements that is contained in the input file
StudentDB_schema_path = sys.argv[1]

# Load the schema from the input file
StudentDB_schema_path = '/Users/euniceolorunshola/Desktop/Database and the Web/Project3/Part4/StudentDBSchema.json'
with open(StudentDB_schema_path) as f:
        #convert from json to python by parsing the json string from the filepath of the input file
    StudentDB_schema_path = json.load(f)

# Iterate over each entity in the schema and generate a MYSQL CREATE TABLE statement
for entity in StudentDB_schema_path["entities"]:
    # Extract the entity name and primary key
    entity_name = entity["name"]
    primary_key = entity["primaryKey"]
    primary_key_const_str = ", ".join(primary_key)
    
    # Generate the CREATE TABLE statements
    create_database_table = f"CREATE TABLE {entity_name} ("
    for attribute in entity["attributes"]:
        # Extract the attribute name, type, and size
        attribute_name = attribute["name"]
        attribute_type = attribute["type"]
        attribute_size = attribute["size"]
        
#define a mapping from data types functions in the schema to corresponding MYSQL type
        map_type = ""
        if attribute_type == "integer":
            map_type = "INT"
        elif attribute_type == "string":
            map_type = f"VARCHAR({attribute_size})"
        
        # Add the attribute to the CREATE TABLE statement
        create_database_table += f"{attribute_name} {map_type}, "
    
    # Add the primary key to the CREATE TABLE statement
    create_database_table += f"PRIMARY KEY ({primary_key_const_str}))"
    
    # Print the CREATE TABLE statements  
    print(create_database_table)
    
# Iterate over any relationship in the schema and generate a CREATE TABLE statement for the relationship's attributes
for relationship in StudentDB_schema_path["relationships"]:
    # Extract the relationship name and attributes
    relationship_name = relationship["name"]
    attributes = relationship["attributes"]
    
    # Generate the CREATE TABLE statements
    create_database_table = f"CREATE TABLE {relationship_name} ("
    for attribute in attributes:
        # Extract the attribute name, type, and size
        attribute_name = attribute["name"]
        attribute_type = attribute["type"]
        attribute_size = attribute["size"]
        
#define a mapping from data types functions in the schema to corresponding MYSQL type
        map_type = ""
        if attribute_type == "integer":
            map_type = "INT"
        elif attribute_type == "string":
            map_type = f"VARCHAR({attribute_size})"
        
        # Add the attribute to the CREATE TABLE statement
        create_database_table += f"{attribute_name} {map_type}, "
    
    # Add foreign key constraints to the CREATE TABLE statement
    for entity in relationship["entities"]:
        # Extract the entity name and cardinality
        entity_name = entity["name"]
        cardinality_cad = entity["cardinality"]
        
        # Add a foreign key constraint to the CREATE TABLE statement
        if cardinality_cad == "one":
            create_database_table += f"FOREIGN KEY ({entity_name}) REFERENCES {entity_name}({primary_key_const_str}), "
        elif cardinality_cad == "many":
            create_database_table += f"FOREIGN KEY ({entity_name}) REFERENCES {entity_name}({primary_key_const_str}) "
    
    # Remove the last comma and space from the CREATE TABLE statement
    create_database_table = create_database_table[:-2]
    
    
    
    # Print the CREATE TABLE statements that includes relationship
    print(create_database_table)
