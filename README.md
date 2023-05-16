# Project3

# Description about this project 
I did this project for my database and the web class as a graduate student 
It contains 4 parts

# Part I : JSON Schema for Schema files 

  Design a JSON Schema(ModelSchema.json) for database schema files such as StudentDBSchema.json. Here are some constraints to be imposed:
  
  * The individual object structures must strictly conform to the keys; i.e., no additional keys or no fewer keys should be allowed.
  * The schema should restrict cardinalities to be one of "one" or "many" and the participation to be one of "mandatory" or "optional".
  * Database, entity, relationship, and attribute names must begin with a letter and may include letters, digits, and underscore characters.  
  
# Part II : Python program to Generate JSON Schema for Instance Files

 Write a Python program (GenerateInstanceSchema.py) that takes as command line argument the name of a database schema file, such as StudentDBModel.json, and outputs to the terminal a JSON Schema file for the database instance files corresponding to the input ER schema. As before, the output schema should strictly enforce the object structures with no additional keys or no fewer keys.
 
  # Steps to access the python file 
  
   1. I used Microsoft Visual Studio Code to code my python program 
   2. I used StudentDBSchema.json file to generate the instance schema.
   3. Put StudentSchema.json and my python file GenerateInstanceSchema.py in the same directory
   4. Replace the file path in line 14 under the comment # load the database schema from the input file with your own file path of your directory that contains StudentDBSchema.json file.
   5. If you are using Microsoft visual studio code run the code by start debugging or go on the terminal and create a directory with the file path that contains the StudentDBSchema.json and GenerateInstanceSchema.py file
   6.  Type the command in the terminal python GenerateInstanceSchema.py  StudentDBSchema.json. This will output the instance schema to the terminal.

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


  # Steps to access the python file 
  
1. Put StudentDBSchema.json, StudentDBInstance.json and my python file GenerateInstanceSchema.py in the same directory.
2. Replace the file path in line 9 under the comment # load the database schema from the input file with your own file path of your directory that contains the StudentDBSchema.json file.
    * Replace the file path in line 15 under the comment # load the generated instance schema from the input file with your own file path of your directory that contains the GenerateInstanceSchema.py file.
    * Replace the file path in line 21 under the comment # load the database instance from the input file with your own file path of your directory that contains the StudentDBInstance.json file
   
 3. If you are using Microsoft visual studio code run the code by start debugging or go on the terminal and create a directory with the file path that contains the StudentDBSchema.json StudentDBInstance.json and GenerateInstanceSchema.py file.
 
 4. Type the command in the terminal python Validate.py StudentDBInstance.json this will first output to check if the database instance file is validated with the generatedinstanceschema file then it will check if all 3 files is validated.
  
 
   # IV : Generate Relational Design

Write a Python program (GenerateRelationalDesign.py) that takes as command line argument the name of a database schema file, such as StudentDBSchema.json, and outputs to the terminal a series of MySQL CREATE TABLE statements that corresponds to the ER Schema using the standard ER-to-Relational mapping.

# Steps to access the python file 

1. Put StudentDBSchema.json and my python file GenerateRelationalDesign.py in the same directory.
2. Replace the file path in line under the comment #load the schema from the input file with your own file path of your directory that contains the StudentDBSchema.json file
3. In the terminal create a directory with the file path that contains the StudentDBSchema.json file
4. Type the command: python GenerateRelationalDesign.py StudentDBSchema.json
This will output the create table statements.
