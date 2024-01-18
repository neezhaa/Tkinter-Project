from tkinter import *
from tkinter import ttk
from subprocess import call
from PIL import Image, ImageTk

app = Tk()
app.title("Stock Management")
app.geometry("800x500")


icon_path = r"D:\ex\project\tkinter-Project\pin.png"
img = Image.open(icon_path)
icon = ImageTk.PhotoImage(img)
app.iconphoto(True, icon)

# in case of the background image doesn't work
app.config(background="black")

# background 
background_image = PhotoImage(file = r"D:\ex\project\tkinter-Project\secondbg.png")
background_label = Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

def Purchase():
  app.destroy()
  call(["python", "purchase.py"])

def Sales():
  app.destroy()
  call(["python", "sales.py"])


head = Label(app, text="Here You Go To Manage Your Stock",font=("Arial", 20, "bold"),fg="black",bg="orange",pady=20,width=300)

label1 =  Label(app, text="Please Choose one of the options :",font=("Arial", 16, "bold"),width="40",bg="black",fg="white")

sales_btn = Button(app , text="Sales",width=25,font=("Arial", 17, "bold"), bg="orange",pady=13, command=Sales)

purchase_btn = Button(app,text="Purchases",width=25, font=("Arial", 17, "bold"),pady=13, bg="orange",command=Purchase)

head.place(relx=0.5, rely=0.08, anchor=CENTER)
label1.place(relx=0.5,rely=0.3,anchor=CENTER)
sales_btn.place(relx=0.5,rely=0.5, anchor=E)
purchase_btn.place(relx=0.5,rely=0.5, anchor=W)

head.pack()

# Execution
app.mainloop()