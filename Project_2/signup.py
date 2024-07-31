from tkinter import *


def registerto():
    import mysql.connector as connector

    con = connector.connect(host='localhost',
                            user='root',
                            password='1234#MD',
                            database='food_ordering')
    global img
    from tkinter import messagebox
    root= Toplevel()
    root.title("Signup")
    root.minsize(height=600, width=900)
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signin():
        root.destroy()
        import loginpage as l
        l.login()

    def signup():
        username = user.get()
        password = code.get()
        conform = confirmcode.get()
        mail=email.get()
        phone_no=phone.get()

        if username == 'username' or password == 'Password' or conform == 'Confirm Password':
            messagebox.showerror("Invalid", "Do not leave any field empty")

        elif password == conform:
            query = "INSERT INTO persons (id, name, password,email, contact_no)  VALUES (8,'{}','{}','{}','{}')".format( username, password, mail, phone_no)
            cur =con.cursor()
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Signup", 'Sucessfully sign up')
            root.destroy()

        else:
            messagebox.showerror("Invalid", "Both Password should match")

    img = PhotoImage(file="signup.png")
    Label(root, image=img, border=0, bg="white").place(x=45, y=90)

    frame = Frame(root, width=350, height=490, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "username")
    Frame(frame, width=240, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    Frame(frame, width=240, height=2, bg='black').place(x=25, y=177)

    confirmcode = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    confirmcode.place(x=30, y=220)
    confirmcode.insert(0, "Confirm Password")
    Frame(frame, width=240, height=2, bg='black').place(x=25, y=245)

    email = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    email.place(x=30, y=290)
    email.insert(0, "Email")
    Frame(frame, width=240, height=2, bg='black').place(x=25, y=315)

    phone = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    phone.place(x=30, y=360)
    phone.insert(0, "Contact Number")
    Frame(frame, width=240, height=2, bg='black').place(x=25, y=385)

    Button(frame, width=39, pady=7, text="Sign Up", bg='#57a1f8', fg="white", border=0, command=signup).place(x=25, y=420)

    label = Label(frame, text="I have an account", fg='black', bg='white', font=("Microsoft YaHei UI Light", 9))
    label.place(x=90, y=460)
    sign_in = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signin)
    sign_in.place(x=200, y=460)
