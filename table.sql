
DROP table IF EXISTS Product;
CREATE table Product(store varchar(30), id integer, type varchar(30));

DROP table IF EXISTS Vegetable;
CREATE table Vegetable(id integer, name varchar(30), price integer);

DROP table IF EXISTS Meat;
CREATE table Meat(id integer, name varchar(30), price integer);

DROP table IF EXISTS Dairy;
CREATE table Dairy(id integer, name varchar(30), price integer);

DROP table IF EXISTS Colonial;
CREATE table Colonial(id integer, name varchar(30), price integer);