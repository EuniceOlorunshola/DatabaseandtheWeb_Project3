# Project3

# Description about this project 
I did this project for my database and the web class as a graduate student 
It contains 4 parts

# Part I : JSON Schema for Schema files 

  Design a JSON Schema(ModelSchema.json) for database schema files such as StudentDBSchema.json.
  
# Part II : Python program to Generate JSON Schema for Instance Files

 Write a Python program (GenerateInstanceSchema.py) that takes as command line argument the name of a database schema file, such as StudentDBModel.json, and outputs to the terminal a JSON Schema file for the database instance files corresponding to the input ER schema. As before, the output schema should strictly enforce the object structures with no additional keys or no fewer keys.
  
# Part III : Validate Instance Files

Write a Python program (Validate.py) to validate an database instance file against the database schema file and the generated instance schema file for both "semantic" as well as "syntactic" errors. The program should first validate the instance file with the generated schema file from previous part for conformity. Then, semantic errors should be caught. The semantic errors in the database schema file are listed below:

* Duplicate entity name
* Duplicate attribute in entity/relationship definition
* Duplicate attribute in primary key
* Key attribute not in entity definition
* Duplicate relationship name
* Entity in relationship not defined

The semantic errors in the database instance file are listed below:

* Data type error in entity or relationship instance
* Primary key in entity error
* Cardinality error in relationship error
* Participation error in relationship error
* Invalid attributes in relationship

# IV : Generate Relational Design

Write a Python program (GenerateRelationalDesign.py) that takes as command line argument the name of a database schema file, such as StudentDBSchema.json, and outputs to the terminal a series of MySQL CREATE TABLE statements that corresponds to the ER Schema using the standard ER-to-Relational mapping.
