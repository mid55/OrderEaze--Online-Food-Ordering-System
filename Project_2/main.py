import tkinter
from tkinter import *

def login():
    import loginpage as l
    l.login()

def openregister():
    import signup as n
    n.registerto()

def menu():
    import search as se
    se.menu()

bg_color = "#F5C6EC"
window = tkinter.Tk()
window.title("Food ordering system")
window.wm_attributes("-transparentcolor")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))
bg = tkinter.PhotoImage(file='images.png')

label17 = tkinter.Label(window, image=bg)
label17.place(x=0, y=0)
label1 = tkinter.Label(bg="black", height=3, width=182)
label1.place(x=0, y=0)
window.config()  # to apply changes to the window
label_text = tkinter.Label(label1, text="Foodies", font=("Arial", 20, "bold"), bg="black", fg="white")
label_text.grid(row=0, column=1)  # for position
dummy_label = Label(label1, bg="black", width=100)
dummy_label.grid(row=0, column=3)
btn1 = tkinter.Button(label1, text="Login", font=("Arial", 12, "bold"), width=8, bg="black", fg="white",command=login)
btn1.grid(column=4, row=0, pady=10, padx=10)
btn2 = tkinter.Button(label1, text="Register", font=("Arial", 12, "bold"), width=8, bg="black", fg="white",command=openregister)
btn2.grid(column=5, row=0, pady=10, padx=10)
btn3 = tkinter.Button(label1, text="Quit", command=window.quit, font=("Arial", 12, "bold"), width=8, bg="black",fg="white")
btn3.grid(column=6, row=0, pady=10, padx=10)
btn4 = tkinter.Button(label1, text="See Menu", font=("Arial", 12, "bold"), width=8, bg="black", fg="white",command=menu)
btn4.grid(column=7, row=0, padx=10)
head_label = tkinter.Label(window, text="Online Food Ordering System", font=("Arial", 40, "bold"), fg="white",bg='grey')
head_label.place(x=300, y=200)
window.mainloop()  # to run the window


