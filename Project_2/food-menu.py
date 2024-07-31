import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Fried Calamari" : 10,
    "Beach Burger" : 14,
    "Salmon Wonder" : 23,
    "Shrimp Tacos" : 15,
    "Sushi Platter" : 25,
    "Empanadas" : 10,
}

root  = Tk()

root.title("Foodies Restaurant")
root_label=Label(root)
root_label.grid(row=0,column=0)
menu_label=Label(root_label,text="Menu",width=30,height=2,bg="grey",font=("Arial",15,"bold"))
menu_label.grid(row=0,column=0)


main_label1=Label(root_label,width=40)
main_label1.grid(row=1,column=0)
dish1=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish1.grid(row=1,column=0)
button1=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button1.grid(row=1,column=1,padx=4,pady=3)

main_label2=Label(root_label,width=40)
main_label2.grid(row=2,column=0)
dish2=Label(main_label2,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish2.grid(row=2,column=0)
button2=Button(main_label2,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button2.grid(row=2,column=1,padx=4,pady=3)

main_label3=Label(root_label,width=40)
main_label3.grid(row=3,column=0)
dish3=Label(main_label3,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish3.grid(row=3,column=0)
button3=Button(main_label3,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button3.grid(row=3,column=1,padx=4,pady=3)

main_label4=Label(root_label,width=40)
main_label4.grid(row=4,column=0)
dish4=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish4.grid(row=4,column=0)
button4=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button4.grid(row=4,column=1,padx=4,pady=3)

main_label5=Label(root_label,width=40)
main_label5.grid(row=5,column=0)
dish5=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish5.grid(row=5,column=0)
button5=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button5.grid(row=5,column=1,padx=4,pady=3)

main_label6=Label(root_label,width=40)
main_label6.grid(row=6,column=0)
dish6=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish6.grid(row=6,column=0)
button6=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button6.grid(row=6,column=1,padx=4,pady=3)

main_label7=Label(root_label,width=40)
main_label7.grid(row=7,column=0)
dish7=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish7.grid(row=7,column=0)
button7=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button7.grid(row=7,column=1,padx=4,pady=3)

main_label8=Label(root_label,width=35)
main_label8.grid(row=8,column=0)
dish8=Label(main_label1,text="1.  Dish 1..............................................$4",fg="white",bg="#2B2B28",width=50,height=2)
dish8.grid(row=8,column=0)
button8=Button(main_label1,text="Display",bg="#2B2B28",height=2,fg="white",width=15)
button8.grid(row=8,column=1,padx=4,pady=3)


display_label=Label(root,text="Display & Description",width=40,bg="blue")
display_label.place(x=2,y=0)


root.mainloop()