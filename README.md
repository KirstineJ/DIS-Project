## Usage
"The Cheapest Link" is a web-app where you can find the cheapest product across Netto, REMA 1000, Føtex, Lidl, Meny. 
You find the cheapest product by typing in your desired product and pressing the button. Currently you can only choose from the following products:

- Apple
- Banana
- Cucumber
- Tomato
- Broccoli
- Chicken
- Ground beef
- Salmon
- Duck
- Pork
- Ribeye
- Milk
- Butter
- Cream
- Skyr
- Yogurt
- Pasta
- Rice
- Salsa
- Oliveoil
- Ketchup
- Mayonnaise

The provided database is self made with no relation to reality. 

## E/R diagram
When updating our E/R diagram we realized that we could have settled with only one table (Product), since the other tables have the same attributes. If we had more time we would have acted on this matter. 

## Requirements:
Run the code below to install the necessary modules.

>$ pip install -r requirements.txt

## Database init
Create a new database in pgAdmin (preferably named CheapGroceries)
1. set the database and your password to pgadmin in app.py file.
2. run table.sql, data.sql in your database.

## Running flask
## The python way

$ python3 run.py

