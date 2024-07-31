from tkinter import *
import mysql.connector as connector

con = connector.connect(host='localhost',
                        user='root',
                        password='1234A#stha',
                        database='food_ordering')


query = 'CREATE TABLE if not exists menu (S_no INT PRIMARY KEY Auto_Increment ,Name VARCHAR(255),description text NOT ' \
        'NULL,Cost float(8,2) NOT NULL) '
cur = con.cursor()
cur.execute(query)


def InsertBlob(id, name, des,cost):
    sqlstatement = "INSERT INTO menu (S_no,Name,description,Cost) VALUES(%s,%s,%s,%s)"
    args=(id, name,des,cost)
    cur = con.cursor()
    cur.execute(sqlstatement,args)
    con.commit()

def delete_table_orders():
    query = "drop table menu"
    cur = con.cursor()
    cur.execute(query)



InsertBlob(1, 'Samosa', 'A samosa or singara is a fried South Asian pastry including ingredients such as spiced potatoes, onions, and peas', 10)
InsertBlob(2, 'Beach Burger', 'Burger Recipe with mix veggie patties, spiced mayo dressing and cucumber, tomato, onion slices.',14)
InsertBlob(3, 'Cheese Fries', 'Cheese fries is a dish consisting of French fries covered in cheese', 23)
InsertBlob(4, 'Pizza', 'A dish of Italian origin, consisting of a flat round base of dough baked with a topping of tomatoes and cheese', 15)
InsertBlob(5, 'Noodles', 'Noodles are a type of staple food made from some type of unleavened dough which is rolled flat and cut into one of a variety of shapes.',25)
# InsertBlob(6,"Fried-Rice","Empanadas description",50)
