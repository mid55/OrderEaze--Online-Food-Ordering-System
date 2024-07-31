from tkinter import *
from datetime import *
import random
global name
orderid = 0
username = ""
flag = 0
phone_no = 0
password=""
import mysql.connector as connector
con = connector.connect(host='localhost',
                        user='root',
                        password='1234#MD',
                        database='food_ordering')
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    order_id = ""
    random_digits = ""
    for i in range(0, 3):
        random_digits += str(random.choice(numbers))

    order_id += random_digits
    return order_id


def login():
    global username

    global img

    from tkinter import messagebox
    root = Toplevel()
    root.title('Login')
    root.minsize(height=500, width=900)
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signup():
        root.destroy()
        import signup as s
        s.registerto()

    def signin():
        global name, orderid,flag,phone_no,username,password
        username = user.get()
        password = code.get()
        query = "select name,password from persons"
        cur = con.cursor()  # to execute the query
        cur.execute(query)
        data = cur.fetchall()

        for d in data:
            if username == d[0] and password == d[1]:
                query = "select contact_no,id from persons where name='{}'".format(username)
                cur = con.cursor()
                cur.execute(query)
                phone_no = cur.fetchall()

                messagebox.showinfo("Valid", "Successfully logged in")
                orderid = ORDER_ID()
                flag = 1
                root.destroy()


        if flag == 0:
            messagebox.showerror("Invalid", "Invalid username or password")

    img = PhotoImage(file="login.png")
    Label(root, image=img, bg="white").place(x=20, y=30)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "username")

    Frame(frame, width=240, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")

    Frame(frame, width=240, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text="Sign in", bg='#57a1f8', cursor='hand2', fg="white", border=0,command=signin).place(x=35,y=204)
    label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=("Microsoft YaHei UI Light", 9))
    label.place(x=78, y=270)
    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup)
    sign_up.place(x=215, y=270)
