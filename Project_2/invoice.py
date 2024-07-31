import tkinter
from tkinter import ttk
import datetime
from tkinter import messagebox
import search
import Bill as b
import loginpage as l

total = 0
id=[]
import mysql.connector as connector

con = connector.connect(host='localhost',
                        user='root',
                        password='1234#MD',
                        database='food_ordering')


def invoice_generator():
    global total, id

    def generate_invoice():
        b.bill()
        messagebox.showinfo("Invoice Complete", "Invoice Complete")

    window = tkinter.Toplevel()
    window.title("Invoice Generator Form")

    frame = tkinter.Frame(window)
    frame.pack(padx=20, pady=10)

    first_name_label = tkinter.Label(frame, text="Name")
    first_name_label.grid(row=0, column=0)

    first_name_entry = tkinter.Label(frame, text=l.username)
    first_name_entry.grid(row=1, column=0)

    phone_label = tkinter.Label(frame, text="Phone")
    phone_label.grid(row=0, column=2)
    phone_entry = tkinter.Label(frame, text=l.phone_no)
    phone_entry.grid(row=1, column=2)

    order_id = l.orderid
    order_label = tkinter.Label(frame, text="order_id")
    order_label.grid(row=2, column=0)
    order_entry = tkinter.Label(frame, text=order_id)
    order_entry.grid(row=3, column=0)

    desc_label = tkinter.Label(frame, text="Address")
    desc_label.grid(row=2, column=1)
    desc_entry = tkinter.Entry(frame, width=40)
    desc_entry.grid(row=3, column=1)

    columns = ('Item-id', 'Item-name', 'price')
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.heading('Item-id', text='Item-id')
    tree.heading('Item-name', text='Item-name')
    tree.heading('price', text='Cost')
    for dt in search.price:
        tree.insert("", 'end', iid=search.price[dt][1], values=(search.price[dt][1], dt, search.price[dt][0]))
        id.append(search.price[dt][1])
    tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

    for dt in search.price:
        total = total + search.price[dt][0]
    total_label1 = tkinter.Label(frame, text="Total Price")
    total_label1.grid(row=6, column=0)
    total_label = tkinter.Label(frame, text=total)
    total_label.grid(row=6, column=1)
    save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
    save_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
    new_invoice_button = tkinter.Button(frame, text="Cancel", command=window.destroy)
    new_invoice_button.grid(row=8, column=0, columnspan=3, sticky="news", padx=20, pady=5)
