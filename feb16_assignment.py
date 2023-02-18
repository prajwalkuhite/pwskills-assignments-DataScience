# Q1

# Database is a collection  of data aaranged in a particular order or in a organised manner.
# Ex.1-- Dictionary-- which is a database in which collection of words arrange in a particular manner.
# Ex-2-- Teleohone directory-- collection of numbers.

#  SQL
# SQL is stands for structured query language we use SQL in a Reational database management system(RDBMS).
# In RDBMS we store the data in the form of tables,rows and columns.
# In SQL fixed schema design and structure used.
# It is vertically scalable and there is a limit to scale.
# This database are best suited for complex queries.
# Widely used databases are MySQl,MSSQL,Oracle etc.

#  NoSQL
# NoSQL stand for NOT Only SQL, it is used in non-relational databases.
# Here we store data in a form Document which is a key value pair data structure.
# In NoSQl dynamic design and structure used.
# It is horizontally scalable with no limit to scale.
# This database are not suited for complex queries.
# Widely used database are MongoDB,cassandra,Neo4j etc.


# Q2

# DDL - Data Definition Language is a set of a SQL commands which can be used to create database schema.
# DDL is used to  create , modify, and delete database structures.
# List of DDL commands:

# 1.CREATE -- This command is used to create database or its object
#             like table,index,function etc. 
# EX-- CREATE database pwskills;
#      By executing.....
# pwskills database created.

# 2.DROP -- This command is used to delete the database or also objects from database.

# 3.ALTER -- This is used to alter the structure of database

# 4.TRUNCATE -- This is used to remove all record from a table including all spaces allocated 
#                for the records are removed.


# Q3

# DML - Data Manupulation Language, The SQL commands that deals with manipulation  of data present in the database.
# By using DML commands we can contols the access to data and to the database.
# List of DML commands:

# 1.INSERT -- This coomand is used to insert the data into a table.
# 
# 2.UPDATE -- This coomand is used to update an existing data within a table.
#
# 3.DELETE -- This command is used to delete records from a database table.


# Q4

# DQL - Data Query Language is used for performing queries on the data within schema objects.
#        This command allows gettind data out of the database to prform operation with it.
#List of DQL commands:
#
# 1. SELECT -- It is used to retrieve data from the database.


# Q5

# Primary Key: 
#            Primary key refers to one of the column in a table which contain a unique and a NOT NUll value.
# The data which entered in the primary column do not contain a dupkicate value also we do not left blank.
# Only one primary key is allowed in a table.
# A database table must have a primary key from which we can do data manipulation.

# Foreign key:
#             A foreign key is a key used to link two tables together also called as referencing key.
# when a column in a one table is playing a role of primary key and the same data column in another 
#  table playing role as non primary ket then that co;umn is known as Foreign key.
# Here for linking minimum two databases are required.
# also here more than one foreign key are allowed in table.


#Q6

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password")

mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# cursor method-- cursor method is used to make a cursor instance in python SQL connection.
# This cursor object helps to execute the query and fetch the records from the database.
# a cursor can be viewed as a pointer to one row in a set of rows.
# 
# Execute method-- the execute method helps us to execute the query and return records 
#                   according to query


# Q7

mycursor = mydb.cursor()
mycursor.execute("Create database if not exists feb16assignment")


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists feb16assignment.february(c1 INT , c2 VARCHAR(10) , c3 INT)")


mycursor.execute("insert into feb16assignment.february values(16,'Feb',2023)")
mydb.commit()


mycursor.execute("select * from feb16assignment.february")



for i in mycursor.fetchall():
    print(i)
mydb.close()