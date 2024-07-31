from tkinter import *

global displayDefaultImage, SamosaImage, burgerImage, friesImage, pizzaImage, sushiImage, empanadasImage
orderid = 0
prices = {}
price = {}
total=0

def menu():
    global prices, price,total
    import tkinter as tk
    from tkinter import ttk
    import random
    from datetime import date
    from datetime import datetime
    import mysql.connector as connector
    from tkinter import messagebox
    import loginpage as l

    con = connector.connect(host='localhost',
                            user='root',
                            password='1234#MD',
                            database='food_ordering')

    from PIL import Image, ImageTk
    global displayDefaultImage, SamosaImage, burgerImage, friesImage, pizzaImage, sushiImage, empanadasImage
    root = Toplevel()
    root.title("Foodies Restaurant")
    query = "select Name,Cost,S_no from menu"
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    for d in data:
        prices[f'{d[0]}'] = [d[1], d[2]]


    # ------------------------------------FUNCTIONS--------------------------------------------- #
    def displaySamosa():
        samosaDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        friesDishFrame.configure(style="DishFrame.TFrame")
        empanadasDishFrame.configure(style="DishFrame.TFrame")
        noodlesDishFrame.configure(style="DishFrame.TFrame")
        pizzaDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")

        displayLabel.configure(
            text="Samosa",
            image=SamosaImage,
            font=('Helvetica', 14, "bold"),
            foreground="white",
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def displayBurger():
        burgerDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        friesDishFrame.configure(style="DishFrame.TFrame")
        empanadasDishFrame.configure(style="DishFrame.TFrame")
        noodlesDishFrame.configure(style="DishFrame.TFrame")
        pizzaDishFrame.configure(style="DishFrame.TFrame")
        samosaDishFrame.configure(style="DishFrame.TFrame")
        displayLabel.configure(
            text="Beach Burger",
            font=('Helvetica', 14, "bold"),
            foreground="white",
            image=burgerImage,
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def displayCheese_Fries():
        friesDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        samosaDishFrame.configure(style="DishFrame.TFrame")
        empanadasDishFrame.configure(style="DishFrame.TFrame")
        noodlesDishFrame.configure(style="DishFrame.TFrame")
        pizzaDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")
        displayLabel.configure(
            text="Cheese Fries",
            font=('Helvetica', 14, "bold"),
            foreground="white",
            image=friesImage,
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def displayPizza():
        pizzaDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        noodlesDishFrame.configure(style="DishFrame.TFrame")
        empanadasDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")
        samosaDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")
        displayLabel.configure(
            text="Pizza",
            font=('Helvetica', 14, "bold"),
            foreground="white",
            image=pizzaImage,
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def displayEmpanadas():
        empanadasDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        pizzaDishFrame.configure(style="DishFrame.TFrame")
        samosaDishFrame.configure(style="DishFrame.TFrame")
        noodlesDishFrame.configure(style="DishFrame.TFrame")
        friesDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")
        displayLabel.configure(
            text="Empanadas",
            font=('Helvetica', 14, "bold"),
            foreground="white",
            image=empanadasImage,
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def displayNoodles():
        noodlesDishFrame.configure(
            relief="sunken",
            style="SelectedDish.TFrame")
        pizzaDishFrame.configure(style="DishFrame.TFrame")
        empanadasDishFrame.configure(style="DishFrame.TFrame")
        samosaDishFrame.configure(style="DishFrame.TFrame")
        friesDishFrame.configure(style="DishFrame.TFrame")
        burgerDishFrame.configure(style="DishFrame.TFrame")
        displayLabel.configure(
            image=sushiImage,
            text="Noodles",
            font=('Helvetica', 14, "bold"),
            foreground="white",
            compound="bottom",
            padding=(5, 5, 5, 5), )

    def add():
        # updating the transaction label
        current_order = orderTransaction.cget("text")
        added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")][0]) + "Rs\n"
        updated_order = current_order + added_dish
        orderTransaction.configure(text=updated_order)
        price[f'{displayLabel.cget("text")}'] = [prices[displayLabel.cget("text")][0],
                                                 prices[displayLabel.cget("text")][1]]

        # updating the order total label
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("Rs", "")
        updated_total = float(order_total) + prices[displayLabel.cget("text")][0]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "Rs")
        total=updated_total

    def delete():
        rec = orderTransaction.cget("text")
        rec = rec.replace("ORDER ID : ", "")
        transaction_list = orderTransaction.cget("text").split("Rs ")
        transaction_list.pop(len(transaction_list) - 1)

    def order():
        new_receipt = orderIDLabel.cget("text")

        new_receipt = new_receipt.replace("ORDER ID : ", "")
        transaction_list = orderTransaction.cget("text").split("Rs ")
        transaction_list.pop(len(transaction_list) - 1)

        order_day = date.today()
        order_time = datetime.now()

        for item in transaction_list:
            item += "Rs "

        orderid = l.orderid
        orderTotalLabel.configure(text="TOTAL : 0Rs")
        orderIDLabel.configure(text="ODER ID: " + str(orderid))
        orderTransaction.configure(text="")
        if orderid == 0:
            messagebox.showerror("Invalid", "Please Login first!")
        else:
            import invoice as i
            i.invoice_generator()

        root.destroy()

    # ---------------------------------- STYLING AND IMAGES ------------------------------------ #
    s = ttk.Style()
    s.configure('MainFrame.TFrame', background="#FFE5CA")
    s.configure('MenuFrame.TFrame', background="#FA9884")
    s.configure('DisplayFrame.TFrame', background="#FA9884")
    s.configure('descriptionFrame.TFrame', background="#FA9884")
    s.configure('DishFrame.TFrame', background="#FA9884", relief="raised")
    s.configure('SelectedDish.TFrame', background="#F9E2AF")
    s.configure('MenuLabel.TLabel',
                background="#E74646",
                font=("Arial", 13, "italic"),
                foreground="white",
                padding=(5, 5, 5, 5),
                width=21)
    s.configure('orderTotalLabel.TLabel',
                background="#FA9884",
                font=("Arial", 10, "bold"),
                foreground="white",
                padding=(2, 2, 2, 2),
                anchor="w"
                )
    s.configure('orderTransaction.TLabel',
                background="#E74646",
                font=('Helvetica', 12),
                foreground="white",
                wraplength=170,
                anchor="nw",
                padding=(3, 3, 3, 3)
                )

    # Menu images
    displayDefaultImageObject = Image.open("food.png").resize((350, 360))
    displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

    SamosaImageObject = Image.open("food-item-1.png").resize((350, 334))
    SamosaImage = ImageTk.PhotoImage(SamosaImageObject)

    burgerImageObject = Image.open("food-item-2.png").resize((350, 334))
    burgerImage = ImageTk.PhotoImage(burgerImageObject)

    friesImageObject = Image.open("food-item-3.png").resize((350, 334))
    friesImage = ImageTk.PhotoImage(friesImageObject)

    pizzaImageObject = Image.open("food-item-4.png").resize((350, 334))
    pizzaImage = ImageTk.PhotoImage(pizzaImageObject)

    noodlesImageObject = Image.open("food-item-5.png").resize((350, 334))
    sushiImage = ImageTk.PhotoImage(noodlesImageObject)

    empanadasImageObject = Image.open("food-item-4.png").resize((350, 334))
    empanadasImage = ImageTk.PhotoImage(empanadasImageObject)

    # ----------------------------------- WIDGETS ----------------------------------------------- #

    mainFrame = ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
    mainFrame.grid(row=0, column=0, sticky="NSEW")
    orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
    orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

    orderTitleLabel = ttk.Label(orderFrame, text="ORDER")
    orderTitleLabel.configure(
        foreground="white", background="#FA9884",
        font=("Helvetica", 14, "bold"), anchor="center",
        padding=(5, 5, 5, 5),
    )
    orderTitleLabel.grid(row=0, column=0, sticky="EW")

    orderIDLabel = ttk.Label(orderFrame, text="ORDER ID : " + str(orderid))
    orderIDLabel.configure(
        background="#E74646",
        foreground="white",
        font=("Helvetica", 11, "italic"),
        anchor="center")
    orderIDLabel.grid(row=1, column=0, sticky="EW", pady=1)

    orderTransaction = ttk.Label(orderFrame, style='orderTransaction.TLabel')
    orderTransaction.grid(row=3, column=0, sticky="NSEW")

    orderTotalLabel = ttk.Label(orderFrame, text="TOTAL : 0Rs", style="orderTotalLabel.TLabel")
    orderTotalLabel.grid(row=4, column=0, sticky="EW")

    menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
    menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

    displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
    displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

    # add order button
    add_order_button = tk.Button(displayFrame, text="Add item", height=1, width=10, bg="red", fg="white",
                                 font=("Arial", 13, "bold"), command=add)
    add_order_button.grid(row=3, column=0, pady=10)

    delete_order_button = tk.Button(displayFrame, text="Delete item", height=1, width=10, bg="red", fg="white",
                                    command=delete,
                                    font=("Arial", 13, "bold"))
    delete_order_button.grid(row=3, column=1, pady=10)

    place_order_button = tk.Button(orderFrame, text="Place your order", height=2, width=20, bg="red", fg="white",
                                   font=("Arial", 13, "bold"), command=order)
    place_order_button.grid(row=5, column=0, pady=50)

    close_button = tk.Button(menuFrame, text="Close-menu", height=2, width=15, bg="red", fg="white",
                             font=("Arial", 13, "bold"), command=root.destroy)
    close_button.grid(row=7, column=0)

    # Dish Frames
    samosaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    samosaDishFrame.grid(row=1, column=0, sticky="NSEW")

    burgerDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    burgerDishFrame.grid(row=2, column=0, sticky="NSEW")

    friesDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    friesDishFrame.grid(row=3, column=0, sticky="NSEW")

    pizzaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    pizzaDishFrame.grid(row=4, column=0, sticky="NSEW")

    noodlesDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    noodlesDishFrame.grid(row=5, column=0, sticky="NSEW")

    empanadasDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
    empanadasDishFrame.grid(row=6, column=0, sticky="NSEW")

    MainMenuLabel = ttk.Label(menuFrame, text="MENU", style="MenuLabel.TLabel")
    MainMenuLabel.grid(row=0, column=0, sticky="WE")
    MainMenuLabel.configure(
        anchor="center",
        font=("Helvetica", 14, "bold"))
    query = "select Name,Cost from menu"
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    for d in data:
        if d[0] == 'Samosa':
            samosaDishLabel = ttk.Label(samosaDishFrame, text=f"Samosa .........{d[1]}Rs", style="MenuLabel.TLabel")
            samosaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        elif d[0] == 'Beach Burger':
            BurgerDishLabel = ttk.Label(burgerDishFrame, text=f"Beach Burger ........{d[1]}Rs",
                                        style="MenuLabel.TLabel")
            BurgerDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        elif d[0] == 'Cheese Fries':
            friesDishLabel = ttk.Label(friesDishFrame, text=f"Cheese Fries ........{d[1]}Rs", style="MenuLabel.TLabel")
            friesDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        elif d[0] == 'Pizza':
            pizzaDishLabel = ttk.Label(pizzaDishFrame, text=f"Pizza ..............{d[1]}Rs", style="MenuLabel.TLabel")
            pizzaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        elif d[0] == 'Noodles':
            noodlesDishLabel = ttk.Label(noodlesDishFrame, text=f"Noodles ...............{d[1]}Rs",
                                         style="MenuLabel.TLabel")
            noodlesDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        elif d[0] == 'Fried-Rice':
            EmpanadasDishLabel = ttk.Label(empanadasDishFrame, text=f"Fried-Rice..........{d[1]}Rs",
                                           style="MenuLabel.TLabel")
            EmpanadasDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    # Buttons
    samosaDisplayButton = ttk.Button(samosaDishFrame, text="Display", command=displaySamosa)
    samosaDisplayButton.grid(row=0, column=1, padx=10)

    BurgerDisplayButton = ttk.Button(burgerDishFrame, text="Display", command=displayBurger)
    BurgerDisplayButton.grid(row=0, column=1, padx=10)

    friesDisplayButton = ttk.Button(friesDishFrame, text="Display", command=displayCheese_Fries)
    friesDisplayButton.grid(row=0, column=1, padx=10)

    pizzaDisplayButton = ttk.Button(pizzaDishFrame, text="Display", command=displayPizza)
    pizzaDisplayButton.grid(row=0, column=1, padx=10)

    noodlesDisplayButton = ttk.Button(noodlesDishFrame, text="Display", command=displayNoodles)
    noodlesDisplayButton.grid(row=0, column=1, padx=10)

    EmpanadasDisplayButton = ttk.Button(empanadasDishFrame, text="Display", command=displayEmpanadas)
    EmpanadasDisplayButton.grid(row=0, column=1, padx=10)

    displayLabel = ttk.Label(displayFrame, image=displayDefaultImage)
    displayLabel.grid(row=0, column=0, sticky="NSEW", columnspan=2)
    displayLabel.configure(background="#FA9884")

    mainFrame.columnconfigure(2, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    menuFrame.columnconfigure(0, weight=1)
    menuFrame.rowconfigure(1, weight=1)
    menuFrame.rowconfigure(2, weight=1)
    menuFrame.rowconfigure(3, weight=1)
    menuFrame.rowconfigure(4, weight=1)
    menuFrame.rowconfigure(5, weight=1)
    menuFrame.rowconfigure(6, weight=1)
