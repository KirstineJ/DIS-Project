
from flask import Flask, render_template, request
import psycopg2



app=Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")


# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="CheapGroceries",
    user="postgres",
    password="password"
)

cursor = conn.cursor()



@app.route("/success.html", methods=['POST'])
def success():
    if request.method == 'POST':
        Input = request.form["Product_name"]

        sql = """ 
        SELECT Product.store, Vegetable.price 
        FROM Product, Vegetable 
        WHERE Product.id = Vegetable.id AND Vegetable.name = %s AND Vegetable.price = (
	        SELECT MIN(price) 
	        FROM Vegetable 
	        WHERE Vegetable.name = %s)
        UNION 
        SELECT Product.store, Meat.price 
        FROM Product, Meat 
        WHERE Product.id =Meat.id AND Meat.name = %s AND Meat.price = (
	        SELECT MIN(price) 
	        FROM Meat 
	        WHERE Meat.name = %s)
        UNION 
        SELECT Product.store, Dairy.price 
        FROM Product, Dairy 
        WHERE Product.id =Dairy.id AND Dairy.name = %s AND Dairy.price = (
	        SELECT MIN(price) 
	        FROM Dairy
	        WHERE Dairy.name = %s)
        UNION 
        SELECT Product.store, Colonial.price 
        FROM Product, Colonial
        WHERE Product.id =Colonial.id AND Colonial.name = %s AND Colonial.price = (
	        SELECT MIN(price) 
	        FROM Colonial
	        WHERE Colonial.name = %s)"""
        
        # Fetch the product information from the database
        cursor = conn.cursor()
        cursor.execute(sql, (Input, Input, Input, Input, Input, Input, Input, Input)) 
        product = cursor.fetchone()
        
        if product:
            product_name, product_price = product
            output="The product, "+str(Input) + ", is cheapest at " + str(product_name) +" and costs "+ str(product_price) + "kr./kg"
        else:
            output="Unfortunately, this product is not supported yet"
        
        return render_template("success.html", output=output)

@app.route("/index.html")
def goback():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()