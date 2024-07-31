import tkinter as tk
from tkinter import *
from tkinter import ttk

import loginpage
from loginpage import *
from datetime import *

global images, img, menu_img


def menu():
    from PIL import Image, ImageTk
    import io
    import random
    import mysql.connector as connector
    con = connector.connect(host='localhost',
                            user='root',
                            password='1234A#stha',
                            database='food_ordering')

    sb = []

    my_w = Tk()
    my_w.geometry("1000x800")

    my_w.columnconfigure(0, weight=8)
    my_w.columnconfigure(1, weight=2)
    my_w.rowconfigure(0, weight=1)
    my_w.rowconfigure(1, weight=14)  # change weight to 4
    my_w.rowconfigure(2, weight=2)

    frame_top = tk.Frame(my_w, bg='white')
    frame_bottom = tk.Frame(my_w, bg='white')

    frame_m_right = tk.Frame(my_w, bg='#f8fab4')
    frame_m_left = tk.Frame(my_w, bg='#284474')

    # placing in grid
    frame_top.grid(row=0, column=0, sticky='WENS', columnspan=2)
    frame_m_left.grid(row=1, column=0, sticky='WENS')
    frame_m_right.grid(row=1, column=1, sticky='WENS')
    frame_bottom.grid(row=2, column=0, sticky='WENS', columnspan=2)
    trv = ttk.Treeview(frame_m_right, selectmode='browse')
    trv.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

    # column identifiers
    trv["columns"] = ("1", "2", "3")
    trv.column("#0", width=80, anchor='w')
    trv.column("1", width=60, anchor='w')
    trv.column("2", width=50, anchor='c')
    trv.column("3", width=50, anchor='c')

    # Headings
    # respective columns
    trv.heading("#0", text="Item", anchor='w')
    trv.heading("1", text="Price", anchor='w')
    trv.heading("2", text="qty", anchor='c')
    trv.heading("3", text="Total", anchor='c')

    def ORDER_ID():
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U',
                   'V', 'W', 'X', 'Y', 'Z']
        order_id = "BIN_"
        random_letters = ""
        random_digits = ""
        for i in range(0, 3):
            random_letters += random.choice(letters)
            random_digits += str(random.choice(numbers))

        order_id += random_letters + random_digits
        return order_id

    def my_reset():
        global total, tax, final
        for item in trv.get_children():
            trv.delete(item)
        l1 = []
        for i in range(8):
            l1.append(tk.IntVar(value=0))
        for i in range(len(sb)):
            sb[i].config(textvariable=l1[i])

        for w in frame_m_right.grid_slaves(1):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(2):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(3):
            w.grid_remove()

        dt = date.today().strftime('%Y-%m-%d')  # todays date
        query = "INSERT INTO  orders (item_id,order_date,total_price) \
                      VALUES (4,%s,%s)"
        data = (dt, final)
        cur = con.cursor()
        cur.execute(query, data)
        lr1 = tk.Button(frame_m_right, text='Bill', font=font1)  # command=lambda:my_invoice(my_w,bill_no,img_top)
        lr1.grid(row=1, column=0, sticky='nw')
        dl = []
        total, tax, final = 0, 0, 0

    def my_bill():
        total = 0
        # print(my_menu)
        for item in trv.get_children():
            trv.delete(item)
        for i in range(len(sb)):
            if (int(sb[i].get()) > 0):
                price = int(sb[i].get()) * my_menu[i][1]
                total = round(total + price, 2)
                my_str1 = (str(my_menu[i][1]), str(sb[i].get()), str(price))
                trv.insert("", 'end', iid=i, text=my_menu[i][0], values=my_str1)
        lr1 = tk.Label(frame_m_right, text='Total', font=font1)
        lr1.grid(row=1, column=0, sticky='nw')
        lr2 = tk.Label(frame_m_right, text=str(total), font=font1)
        lr2.grid(row=1, column=1, sticky='nw')
        lr21 = tk.Label(frame_m_right, text='Tax 10%', font=font1)
        lr21.grid(row=2, column=0, sticky='nw')
        tax = round(0.1 * total, 2)
        lr22 = tk.Label(frame_m_right, text=str(tax), font=font1)
        lr22.grid(row=2, column=1, sticky='nw')
        lr31 = tk.Label(frame_m_right, text='Total', font=font2)
        lr31.grid(row=3, column=0, sticky='nw')
        final = round(total + tax, 2)
        lr32 = tk.Label(frame_m_right, text=str(final), font=font2)
        lr32.grid(row=3, column=1, sticky='nw')
        return final

    font1 = ('Times', 14, 'normal')
    font2 = ('Times', 32, 'bold')
    pdx, pdy = 1, 5
    my_menu = {}  # Dictionary to store items with price
    sb = []
    r, c, i = 0, 0, 0

    def show_items():
        global r, c, i, my_menu
        my_menu.clear()  # remove all items
        sb.clear()
        r, c, i = 0, 0, 0
        cur = con.cursor()
        # cur.execute(query)
        query = "SELECT * FROM menu"
        cur.execute(query)
        r_set = cur.fetchall()
        global images
        images = []
        for item in r_set:
            global img
            img = Image.open(io.BytesIO(item[2]))
            img = ImageTk.PhotoImage(img)
            images.append(img)

        for img in images:
            global menu_img
            menu_img = tk.Label(frame_m_left, image=img)
            menu_img.grid(row=r, column=c, padx=pdx, pady=0)

            if c > 1:  # add one more row
                c = 0
                r = r + 2
            else:
                c = c + 1

        for item in r_set:
            # global img
            # img = Image.open(io.BytesIO(item[2]))
            # img = ImageTk.PhotoImage(img)
            #
            # menu_img=tk.Label(frame_m_left,image=img )
            # menu_img.grid(row=r, column=c, padx=pdx, pady=0)
            menu = tk.Label(frame_m_left, text=f"{item[1]}({item[4]})", font=font1)
            menu.grid(row=r + 1, column=c, padx=pdx, pady=0)
            r1 = r + 1
            sbox = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font2, width=1)
            sbox.grid(row=r1, column=c, padx=pdx, pady=0)
            sb.append(sbox)
            my_menu[i] = [item[1], item[4]]
            i = i + 1

            if c > 1:  # add one more row
                c = 0
                r = r + 2
            else:
                c = c + 1

    show_items()
    r = r + 1
    r1_v = tk.IntVar(value=1)  # We used integer variable here

    b1 = tk.Button(frame_bottom, text='Get Bill', command=my_bill)
    b1.grid(row=r, column=3, padx=10)
    b2 = tk.Button(frame_bottom, text='Confirm ( Reset)', command=my_reset)
    b2.grid(row=r, column=4, padx=10)
    my_w.mainloop()
menu()