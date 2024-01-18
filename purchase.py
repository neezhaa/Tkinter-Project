from tkinter import *
from subprocess import call
from tkinter import messagebox
import csv
from tkinter import ttk
from PIL import Image, ImageTk

main = Tk()
main.geometry("2000x1000")
main.title("Purchases")

icon_path = r"D:\ex\project\tkinter-Project\pin.png"
img = Image.open(icon_path)
icon = ImageTk.PhotoImage(img)
main.iconphoto(True, icon)


main.configure(bg="black")
background_image = PhotoImage(file = r"D:\ex\project\tkinter-Project\secondbg.png")
background_label = Label(main, image=background_image)
background_label.place(relwidth=1, relheight=1)

csv_header = ["ID","supplier","phone","product_name","price","quantity"]
file = open(r"purchases.csv", "a+")
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
  

  tree.insert('', 'end', values=(product_id, supplier_id, phone,product_name,price,quantity)) 

  # clear entry
  product_id_input.delete(0,END)
  supplier_input.delete(0,END)
  phone_input.delete(0,END)
  product_name_input.delete(0,END)
  price_input.delete(0,END)
  quantity_input.delete(0,END)
  
  # TO Validate input fields
  if not product_id or not supplier_id or not phone or not product_name or not price  or not quantity:
    messagebox.showerror("Error", "All fields are required.")
    return

  try:
    # HERE Writing data to the purchases.csv file
    writer = csv.writer(file, delimiter=',', lineterminator="\r")
    writer.writerow([product_id,supplier_id,phone,product_name,price,quantity])

    #success message
    messagebox.showinfo("Success", "Purchase saved successfully.")

  except Exception as error:
    messagebox.showerror("Error", error)

# Create a Treeview widget
tree = ttk.Treeview(main, columns=('ID', 'Supplier', 'Phone','Product Name', 'Price','Quantity'), show='headings')
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11))  # You can adjust the font family and size

# Define column headings
tree.heading('ID', text='ID')
tree.heading('Supplier', text='Supplier')
tree.heading('Phone', text='Phone')
tree.heading('Product Name', text='Product Name')
tree.heading('Price', text='Price')
tree.heading('Quantity', text='Quantity')

# Specify column widths
tree.column('ID', width=136)
tree.column('Supplier', width=136)
tree.column('Phone', width=136)
tree.column('Product Name', width=136)
tree.column('Price', width=136)
tree.column('Quantity', width=136)

# Pack the Treeview widget
tree.place(x=680, y= 390, anchor=W, width=837, height=600)


def back():
  main.destroy()
  call(["python", r"C:\Users\hp\Desktop\tkinter\projet\principal.py"])



def remove_selected_row():
  # Get the selected item
  selected_item = tree.selection()

  if selected_item:
    result = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete?")
    if result:
      # Delete the selected item
      tree.delete(selected_item)



def remove_row_by_id():
  # Get the ID entered in the entry widget
  id = product_id_input.get()

  # Find the item with the specified ID
  item_to_delete = None
  for item in tree.get_children():
    if tree.item(item, "values")[0] == id:
        item_to_delete = item
        break

  # Delete the item if found
  if item_to_delete:
    result = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete?")
    if result :
        tree.delete(item_to_delete)
  else:
    # Display a message if the ID is not found
    product_id_input.config(text=f"Article with ID {id} not found", fg="red")


def clear_entries():
  product_id_input.delete(0,END)
  supplier_input.delete(0,END)
  phone_input.delete(0,END)
  product_name_input.delete(0,END)
  price_input.delete(0,END)
  quantity_input.delete(0,END)

def edit():
  selected_item = tree.selection()
  if selected_item:
      # Retrieve data from the selected item
      item_values = tree.item(selected_item, 'values')

      # Populate entry widgets with the selected data
      product_id_input.insert(0, item_values[0])
      supplier_input.insert(0, item_values[1])
      phone_input.insert(0, item_values[2])
      product_name_input.insert(0, item_values[3])
      price_input.insert(0, item_values[4])
      quantity_input.insert(0, item_values[5])

      # Delete the selected item from the treeview
      tree.delete(selected_item)

head = Label(main, text="> Purchases",font=("Arial", 20, "bold"),fg="white",bg="orange",pady=20,width=300)


product_id = Label(main, text="Product ID", font=("Arial", 16), bg="black", fg="white")
supplier = Label(main, text="supplier", font=("Arial", 16), bg="black", fg="white")
phone = Label(main, text="Phone", font=("Arial", 16), bg="black", fg="white")
product_name = Label(main, text="Product Name", font=("Arial", 16), bg="black", fg="white")
price = Label(main, text="Price", font=("Arial", 16), bg="black", fg="white")
quantity = Label(main, text="Quantity", font=("Arial", 16), bg="black", fg="white")

product_id_input = Entry(main)
supplier_input = Entry(main)
phone_input = Entry(main)
product_name_input = Entry(main)
price_input = Entry(main)
quantity_input = Entry(main)

# save button
save_btn = Button(main, text="Save Record", bg="black",font=("Arial", 14),fg="orange", command=save)
save_btn.place(x=80, y= 400, anchor=W, width=200, height=50)
save_btn.config(cursor="hand2")

# clear button
clear_btn = Button(main, text="Clear Entry", bg="black",font=("Arial", 14),fg="orange", command=clear_entries)
clear_btn.place(x=290, y= 400, anchor=W, width=200, height=50)
clear_btn.config(cursor="hand2")

# remove row by id
remove_btn_by_id = Button(main, text="Remove by id", bg="black", font=("Arial", 14), fg="orange", command=remove_row_by_id)
remove_btn_by_id.place(x=80, y= 460, anchor=W, width=200, height=50)
remove_btn_by_id.config(cursor="hand2")

#remove row by selection
remove_selected_item_btn = Button(main, text="Remove Selected Row", bg="black", font=("Arial", 13), fg="orange", command=remove_selected_row)
remove_selected_item_btn.place(x=290, y= 460, anchor=W, width=200, height=50)
remove_selected_item_btn.config(cursor="hand2")

# edit button
edit_btn = Button(main, text="Edit", bg="black", font=("Arial", 14), fg="orange", command=edit)
edit_btn.place(x=80, y= 520, anchor=W, width=200, height=50)
edit_btn.config(cursor="hand2")

# back button
back_btn = Button(main, text="Back", bg="black", font=("Arial", 14), fg="orange", command=back)
back_btn.place(x=290, y= 520, anchor=W, width=200, height=50)
back_btn.config(cursor="hand2")

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

main.mainloop()