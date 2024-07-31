from tkinter import *


def bill():
    import tkinter
    from tkinter import ttk
    import search
    import invoice as i
    import loginpage as l
    import mysql.connector as connector
    import datetime as dt
    con = connector.connect(host='localhost',
                            user='root',
                            password='1234#MD',
                            database='food_ordering')

    def action():
        import my_invoice_with_qr as m
        m.qrcode()

    root = Toplevel()
    root.minsize(height=500, width=500)
    mainlabel = Label(root, text="THANK YOU FOR ORDERING! 🙏 🙏", font=("Arial", 30))
    mainlabel.grid(row=0, column=2,padx=20,pady=30)
    frame1 = tkinter.Frame(root, height=100, width=100)
    frame1.grid(row=1, column=2)
    frame2 = tkinter.Frame(root, height=300, width=500)
    frame2.grid(row=2, column=2)
    name_label = tkinter.Label(frame1, text="Name: ")
    name_label.grid(row=0, column=0)
    phone_label = tkinter.Label(frame1, text="Contact Number: ")
    phone_label.grid(row=1, column=0)
    total_label = tkinter.Label(frame2, text=f" Total Price: {i.total}")
    total_label.grid(row=2, column=0)
    pay_button = tkinter.Button(frame2, text="Go for payment", bg="blue", fg="white", command=action)
    pay_button.grid(row=2, column=2)
    name = tkinter.Label(frame1, text=l.username)
    name.grid(row=0, column=1)
    phone = tkinter.Label(frame1, text=l.phone_no)
    phone.grid(row=1, column=1)
    columns = ('Item-id', 'Item-name', 'price')
    tree = ttk.Treeview(frame2, columns=columns, show="headings")
    tree.heading('Item-id', text='Item-id')
    tree.heading('Item-name', text='Item-name')
    tree.heading('price', text='Cost')
    for dt in search.price:
        tree.insert("", 'end', iid=search.price[dt][1], values=(search.price[dt][1], dt, search.price[dt][0]))
    tree.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

