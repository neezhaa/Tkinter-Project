from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter import ttk
import csv

main = Tk()
main.geometry("2000x500")
main.title("Sales")
# main.resizable(True, False)
main.configure(bg="#219ebc")

background_image = PhotoImage(file = r"D:\ex\project\tkinter-Project\secondbg.png")
background_label = Label(main, image=background_image)
background_label.place(relwidth=1, relheight=1)


csv_header = ["ID","client","phone","product_name","s_Price","quantity"]
file = open(r"D:\ex\project\tkinter-Project\sales.csv", "a")
writer = csv.writer(file, delimiter=',', lineterminator="\r")

#if the file is empty write the header 
if file.tell() == 0:
    writer.writerow(csv_header)



def save():
  product_id = product_id_input.get()
  client_id = client_input.get()
  phone = phone_input.get()
  product_name = product_name_input.get()
  s_Price = s_Price_input.get()
  quantity = quantity_input.get()
  
  # Insert data into the treeview
  tree.insert('', 'end', values=(product_id, client_id, phone,product_name,s_Price,quantity)) 
  

  # TO Validate input fields
  if not product_id or not client_id or not phone or not product_name or not s_Price  or not quantity:
    messagebox.showerror("Error", "All fields are required.")
    return

  try:
    # HERE Writing data to the sales.csv file
    writer = csv.writer(file, delimiter=',', lineterminator="\r")
    writer.writerow([product_id,client_id,phone,product_name,s_Price,quantity])

    #hna message
    messagebox.showinfo("Success", "Sale saved successfully.")

  except Exception as error:
    messagebox.showerror("Error", error)

# copy data to the table

def back():
  main.destroy()
  call(["python", r"D:\ex\project\tkinter-Project\menu.py"])


def clear_entries():
  product_id_input.delete(0,END)
  client_input.delete(0,END)
  phone_input.delete(0,END)
  product_name_input.delete(0,END)
  s_Price_input.delete(0,END)
  quantity_input.delete(0,END)


# Create a Treeview widget
tree = ttk.Treeview(main, columns=('ID', 'client', 'phone','name', 'price','quantity'), show='headings')

# Define column headings
tree.heading('ID', text='ID')
tree.heading('client', text='client')
tree.heading('phone', text='phone')
tree.heading('name', text='name')
tree.heading('price', text='price')
tree.heading('quantity', text='quantity')

# Specify column widths
tree.column('ID', width=136)
tree.column('client', width=136)
tree.column('phone', width=136)
tree.column('name', width=136)
tree.column('price', width=136)
tree.column('quantity', width=136)

# Pack the Treeview widget
tree.place(x=680, y= 390, anchor=W, width=837, height=600)

head = Label(main, text="> Sales",font=("Arial", 20, "bold"),fg="white",bg="orange",pady=20,width=300)


product_id = Label(main, text="Product ID", font=("Arial", 16), bg="black", fg="white")
client = Label(main, text="Client", font=("Arial", 16), bg="black", fg="white")
phone = Label(main, text="Phone", font=("Arial", 16), bg="black", fg="white")
product_name = Label(main, text="Product Name", font=("Arial", 16), bg="black", fg="white")
s_Price = Label(main, text="Price", font=("Arial", 16), bg="black", fg="white")
quantity = Label(main, text="Quantity", font=("Arial", 16), bg="black", fg="white")

product_id_input = Entry(main)
client_input = Entry(main)
phone_input = Entry(main)
product_name_input = Entry(main)
s_Price_input = Entry(main)
quantity_input = Entry(main)


# buttons save and clear
save_btn = Button(main, text="Save Record", bg="black", font=("Arial", 14),fg="orange", command=save)
save_btn.place(x=80, y= 400, anchor=W, width=190, height=50)

clear_btn = Button(main, text="Clear Entry", bg="black", font=("Arial", 14),fg="orange", command=clear_entries)
clear_btn.place(x=280, y= 400, anchor=W, width=190, height=50)


# buttons edit/ remove / retour message box/ 

remove_btn = Button(main, text="Remove", bg="black", font=("Arial", 14), fg="orange")
remove_btn.place(x=1000, y= 750, anchor=E, width=140, height=50)

back_btn = Button(main, text="Back", bg="black", font=("Arial", 14), fg="orange", command=back)
back_btn.place(x=1150, y= 750, anchor=E, width=140, height=50)



head.place(x=150,y=30, anchor=CENTER)
product_id.place(x=140, y= 120, anchor=E)
product_id_input.place(x=280, y= 120, anchor=W, width=250, height=30)

client.place(x=90, y= 160, anchor=E)
client_input.place(x=280, y= 160, anchor=W, width=250, height=30)

phone.place(x=98, y= 200, anchor=E)
phone_input.place(x=280, y= 200, anchor=W, width=250, height=30)

product_name.place(x=103, y= 240, anchor=CENTER)
product_name_input.place(x=280, y= 240, anchor=W, width=250, height=30)

s_Price.place(x=89, y= 280, anchor=E)
s_Price_input.place(x=280, y= 280, anchor=W, width=250, height=30)

quantity.place(x=118, y= 320, anchor=E)
quantity_input.place(x=280, y= 320, anchor=W, width=250, height=30)

main.mainloop()
