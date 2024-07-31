from tkinter import *

global Image, Image2


def qrcode():
    global Image,Image2
    from PIL import Image, ImageTk
    root = Toplevel()
    root.minsize(height=400, width=800)
    root.config(bg="#B9EDDD")
    main_label = Label(root, text="Your Food is on Wheels! 😍 😍", font=("Arial", 20), bg="#B9EDDD")
    main_label.grid(row=0, column=0)
    ImageObject = Image.open("qrcode.png").resize((350, 334))
    Image = ImageTk.PhotoImage(ImageObject)
    image_label = Label(root, image=Image, bg="#B9EDDD")
    image_label.grid(row=1, column=0, padx=100)
    Image2 = PhotoImage(file="delivery.png")
    image2_label = Label(root, image=Image2,bg="#B9EDDD")
    image2_label.grid(row=1, column=1)
