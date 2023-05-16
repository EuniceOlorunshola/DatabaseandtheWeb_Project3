#imported json module
import json
#imported internal python module
import sys
# used for validation of schema in python
import jsonschema

# Read the schema file name from the command line argument
#if length of the argument in the command line is less then 2 it shows the print statement
if len(sys.argv) < 2:
    print("Python Program file and database instance file  should be included in the command line argument in the terminal Ex: Validate.py StudentDBInstance.json")
    exit()
    #Displays the command line arguments by extracting all the elements that is contained in the input file 
#StudentDB_schema_path = sys.argv[1]
instance_DB_path = sys.argv[1]
# Load the database schema from the input file
StudentDB_schema_path = '/Users/euniceolorunshola/Desktop/Database and the Web/Project3/Part3/StudentDBSchema.json'
with open(StudentDB_schema_path) as f:
#convert from json to python by parsing the json string from the filepath of the input file
 StudentDB_schema_path = json.load(f)

# load the generated instance schema from the input file
generate_instance_schema_path = '/Users/euniceolorunshola/Desktop/Database and the Web/Project3/Part3/GenerateInstanceSchema.py'
with open(generate_instance_schema_path) as f:
 #convert from json to python by parsing the json string from the filepath of the input file
 generate_instance_schema_path = json.load(f)

# load the database instance from the input file
instance_DB_path = '/Users/euniceolorunshola/Desktop/Database and the Web/Project3/Part3/StudentDBInstance.json'
with open(instance_DB_path) as f:
#convert from json to python by parsing the json string from the filepath of the input file
 instance_DB_path = json.load(f)

 # first validate the database instance file against the generated instance schema file
 jsonschema.validate(instance_DB_path, generate_instance_schema_path)

 # second validate the database instance file against the database schema file
 jsonschema.validate(instance_DB_path, StudentDB_schema_path)

 # Semantic errors should be checked in both schema and instance file

# Catch the semantic errors in the database schema file 
entity_names = set()
entity_attributes = {}
entity_primarykeys = {}
relationship_names = set()
relationship_entities = {}
relationship_attributes = set()
relationship_properties = set()
for entity in StudentDB_schema_path["entities"]:
 # check for duplicate entity name
 entity_name = entity["name"]
 if entity_name in entity_names: 
  print("Semantic Error Caught: Duplicate entity name - " + entity_name)
 else:
  entity_names.add(entity_name)
  entity_attributes[entity_name] = set()
  entity_primarykeys[entity_name] = set()
  for attribute in entity["attributes"]:
   # check for duplicate attributes in entity 
   if attribute["name"] in entity_attributes[entity["name"]]:
    print("Semantic error Caught: Duplicate attribute in entity: {attribute['name']} in entity: [entity['name']}")
    entity_attributes[entity["name"]].append(attribute["name"])

    # check for duplicate attribute in primary key
primaryKeys_attribute_names = [primaryKeys_attribute['name'] for primaryKeys_attribute in entity ['primaryKey']]
if len(primaryKeys_attribute_names) != len(set(primaryKeys_attribute_names)): 
 print("Semantic Error Caught: Duplicate attribute detected in primary key")
 primaryKeys_attribute_names.add(attribute["name"])

 # check for key attribute not in entity definition 
 if attribute["Keys"] and attribute["name"] not in entity_attributes[entity["name"]]:
  print("Sematic Error Caught: Key attribute {attribute['name]} not in entity {entity['name']}")

for relationship in StudentDB_schema_path["relationships"]:
 # check for duplicate relationship name
 if relationship["name"] in relationship_names:
  print("Semantic Error Caught: Duplicate relationship name detected {relationship['name']}")
 else:
  relationship_names.add(relationship["name"])
  relationship_attributes[relationship["name"]]

  # check for entity in relationship not defined
for entity in relationship["entities"]:
 entity_name = entity['entity']
 if entity_name not in entity_names:
  print("Semantic Error Caught: Entity in relationship detected is not defined - " + entity_name)


  # Next is to catch the semantic errors in the database instance file

  #  check for data type error in entity or relationship  instance
  for entity in instance_DB_path["entities"]:
   for attribute in entity:
    if not isinstance(entity[attribute], StudentDB_schema_path["entities"][entity["entity"]]["attributes"][attribute]["type"]):
     print("Semantic Error Caught: Data type error is detected in entity instance {entity['entity']} attribute {attribute}")

     # check for primary key in entity error 
     PrimaryKey_attributes = [attribute for attribute in StudentDB_schema_path["entities"][entity["entity"]]["attributes"] if attribute["primaryKey"]]
     if not all(attribute in entity for attribute in PrimaryKey_attributes):
      print("Semantic Error Caught: Primary key error detected in entity {entity['entity]}")

      # check for cardinality error in relationship error 
      for instance in instance_DB_path[relationship_names]:
       cardinality_entity_first = relationship_properties["cardinality_entity_first"]
       cardinality_entity_second = relationship_properties["cardinality_entity_second"]
       cardinality = relationship_properties["cardinality"]
       if cardinality == "one to one":
        if len(instance[cardinality_entity_first]) != 1 or len(instance[cardinality_entity_second]) != 1:
         print("Semantic Error Caught: Cardinality error detected in relationship error expected one to one relationship")
       elif  cardinality == "one to many":
        if len(instance[cardinality_entity_first]) != 1 or len(instance[cardinality_entity_second]) == 0:
         print("Semantic Error Caught: Cardinality error detected in relationship error expected one to many relationship")
        elif  cardinality == "many to one":
         if len(instance[cardinality_entity_first]) == 0 or len(instance[cardinality_entity_second]) != 1:
          print("Semantic Error Caught: Cardinality error detected in relationship error expected many to one relationship") 
        elif  cardinality == "many to many":
         if len(instance[cardinality_entity_first]) == 0 or len(instance[cardinality_entity_second]) == 0:
          print("Semantic Error Caught: Cardinality error detected in relationship error expected many to many relationship") 

          # check for participation error in relationshop error 
          if "participation" in StudentDB_schema_path["relationships"] and entity not in StudentDB_schema_path["relationships"]["participation"]:
           print("Semantic error Caught: Participation error detected in relationship")


          # check for invalid attributes in relationship
          for relationship in instance_DB_path:
           if relationship["type"] == "relationship": 
            if relationship["name"] in StudentDB_schema_path:
             valid_attributes = StudentDB_schema_path[relationship["name"]]["entities"][0]["attributes"] and  StudentDB_schema_path[relationship["name"]]["entities"][1]["attributes"]
    

 






