from tkinter import *
from subprocess import call
from tkinter import messagebox
import csv

purchases = Tk()
purchases.geometry("2000x500")
purchases.title("Purchases")
# purchases.resizable(True, False)
purchases.configure(bg="#219ebc")

background_image = PhotoImage(file = r"c:\Users\hp\Desktop\secondbg.png")
background_label = Label(purchases, image=background_image)
background_label.place(relwidth=1, relheight=1)


csv_header = ["ID","supplier","phone","product_name","price","quantity"]
file = open(r"C:\Users\hp\Desktop\tkinter\projet\purchases.csv", "a")
writer = csv.writer(file, delimiter=',', lineterminator="\r")

#if the file is empty write the header 
if file.tell() == 0:
    writer.writerow(csv_header)



def save():
  product_id = product_id_input.get()
  supplier_id = supplier_input.get()
  phone = phone_input.get()
  product_name = product_name_input.get()
  price = price_input.get()
  quantity = quantity_input.get()
  print(product_id,supplier_id,phone,product_name,price,quantity)
  

  # TO Validate input fields
  if not product_id or not supplier_id or not phone or not product_name or not price  or not quantity:
    messagebox.showerror("Error", "All fields are required.")
    return

  try:
    # HERE Writing data to the purchases.csv file
    writer = csv.writer(file, delimiter=',', lineterminator="\r")
    writer.writerow([product_id,supplier_id,phone,product_name,price,quantity])

    #hna message
    messagebox.showinfo("Success", "Sale saved successfully.")

  except Exception as error:
    messagebox.showerror("Error", error)

# copy data to the table

def back():
  purchases.destroy()
  call(["python", r"C:\Users\hp\Desktop\tkinter\projet\principal.py"])


def clear_entries():
  product_id_input.delete(0,END)
  supplier_input.delete(0,END)
  phone_input.delete(0,END)
  product_name_input.delete(0,END)
  price_input.delete(0,END)
  quantity_input.delete(0,END)


head = Label(purchases, text="> Purchases",
              font=("Arial", 20, "bold"),
              fg="white",
              bg="orange",
              pady=20,
              width=300)


#display data 
data = Label(purchases, bg="white")
data.place(x=680, y= 390, anchor=W, width=820, height=600)

id = Label(data, text="ID", bg="grey", font=("Arial", 12))
id.place(x=-2, y= 16, anchor=W, width=136, height=36)

supplier = Label(data, text="supplier", bg="grey", font=("Arial", 12))
supplier.place(x=135, y= 16, anchor=W, width=136, height=36)

phone = Label(data, text="phone", bg="grey", font=("Arial", 12))
phone.place(x=272, y= 16, anchor=W, width=136, height=36)

name = Label(data, text="name", bg="grey", font=("Arial", 12))
name.place(x=409, y= 16, anchor=W, width=136, height=36)

price = Label(data, text="price", bg="grey", font=("Arial", 12))
price.place(x=546, y= 16, anchor=W, width=136, height=36)

quantity = Label(data, text="quantity", bg="grey", font=("Arial", 12))
quantity.place(x=683, y= 16, anchor=W, width=136, height=36)




product_id = Label(purchases, text="Product ID", font=("Arial", 16), bg="black", fg="white")
supplier = Label(purchases, text="supplier", font=("Arial", 16), bg="black", fg="white")
phone = Label(purchases, text="phone", font=("Arial", 16), bg="black", fg="white")
product_name = Label(purchases, text="Product Name", font=("Arial", 16), bg="black", fg="white")
price = Label(purchases, text="Price", font=("Arial", 16), bg="black", fg="white")
quantity = Label(purchases, text="Quantity", font=("Arial", 16), bg="black", fg="white")

product_id_input = Entry(purchases)
supplier_input = Entry(purchases)
phone_input = Entry(purchases)
product_name_input = Entry(purchases)
price_input = Entry(purchases)
quantity_input = Entry(purchases)


# buttons save and clear
save_btn = Button(purchases, text="Save Record", bg="black", font=("Arial", 14),fg="orange", command=save)
save_btn.place(x=80, y= 400, anchor=W, width=190, height=50)

clear_btn = Button(purchases, text="Clear Entry", bg="black", font=("Arial", 14),fg="orange", command=clear_entries)
clear_btn.place(x=280, y= 400, anchor=W, width=190, height=50)


# buttons edit/ remove / retour message box/ 

remove_btn = Button(purchases, text="Remove", bg="black", font=("Arial", 14), fg="orange")
remove_btn.place(x=1000, y= 750, anchor=E, width=140, height=50)

back_btn = Button(purchases, text="Back", bg="black", font=("Arial", 14), fg="orange", command=back)
back_btn.place(x=1150, y= 750, anchor=E, width=140, height=50)



head.place(x=150,y=30, anchor=CENTER)
product_id.place(x=140, y= 120, anchor=E)
product_id_input.place(x=280, y= 120, anchor=W, width=250, height=30)

supplier.place(x=114, y= 160, anchor=E)
supplier_input.place(x=280, y= 160, anchor=W, width=250, height=30)

phone.place(x=98, y= 200, anchor=E)
phone_input.place(x=280, y= 200, anchor=W, width=250, height=30)

product_name.place(x=103, y= 240, anchor=CENTER)
product_name_input.place(x=280, y= 240, anchor=W, width=250, height=30)

price.place(x=89, y= 280, anchor=E)
price_input.place(x=280, y= 280, anchor=W, width=250, height=30)

quantity.place(x=118, y= 320, anchor=E)
quantity_input.place(x=280, y= 320, anchor=W, width=250, height=30)

purchases.mainloop()
