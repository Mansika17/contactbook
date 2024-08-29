from tkinter import *
from tkinter import messagebox
import re


contacts = []

def p_valid(p):
    return p.isdigit() and len(p) == 10

def e_valid(e) :
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern , e)
    

def add_c():
    n = namee.get().strip()
    p = phonee.get().strip()
    e = emaile.get().strip()
    a = addresse.get().strip()
    if not n or not p:
        messagebox.showwarning("Input Error", "Name and Phone Number is MANDATORY!")
        return 
    if not p_valid(p):
        messagebox.showwarning("Input Error" ,"Please Enter A Valid Phone Number!")
    if not e_valid(e):
        messagebox.showwarning("Input Error" , "Please Enter A Valid Email!")

    contact = {
        "name": n,
        "phone": p,
        "email": e,
        "address": a,
    }
    contacts.append(contact)
    refresh_cl()
    clear_all()
    messagebox.showinfo("Success", f"Contact '{n}' added successfully.")

def view_c(event):
    selected_index = cl.curselection()
    if selected_index:
        contact= contacts[selected_index[0]]
        namee.delete(0, END)
        namee.insert(0, contact['name'])
        phonee.delete(0, END)
        phonee.insert(0, contact['phone'])
        emaile.delete(0, END)
        emaile.insert(0, contact['email'])
        addresse.delete(0, END)
        addresse.insert(0, contact['address'])

def search_c():
    search_contact =searche.get().strip().lower()
    result =[]
    for contact in contacts:
        if search_contact in contact['name'].lower() or search_contact in contact['phone']:
            result.append(contact)
        cl.delete(0 , END)
    for contact in result:
       cl.insert(END , f"{contact['name']}-{contact['phone']}")
    

def update_c():
    selected_c = cl.curselection()
    if selected_c:
        n = namee.get().strip()
        p= phonee.get().strip()
        e = emaile.get().strip()
        a = addresse.get().strip()
        
        if not n or not p:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")
            return
        
        contacts[selected_c[0]] = {
            "name": n,
            "phone": p,
            "email": e,
            "address": a,
        }
        refresh_cl()
        clear_all()
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

def delete_c():
    selected_c = cl.curselection()
    if selected_c:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            deleted_c = contacts.pop(selected_c[0])
            refresh_cl()
            clear_all()
            messagebox.showinfo("Successfull!!", f"Contact '{deleted_c['name']}' deleted successfully.")
    else:
       messagebox.showwarning("Select Contact"," Have to select a conatact to delete !")

def refresh_cl():
    cl.delete(0,END)
    for contact in contacts:
        cl.insert(END, f"{contact['name']} - {contact['phone']}")

def clear_all():
    namee.delete(0,END)
    phonee.delete(0,END)
    emaile.delete(0 , END)
    addresse.delete(0 , END)
    searche.delete(0 , END)  

def clear_search():
    searche.delete(0, END)
    refresh_cl()
   
application_window = Tk()
application_window.title("CONTACT BOOK")
application_window.geometry("700x550")
application_window.config(bg = "grey")

heading = Label(application_window , text ="CONTACT BOOK" , bg = "lightblue")
heading.pack(pady = 5)

i_f = Frame(application_window)
i_f.pack(pady= 10)

b_f = Frame(application_window)
b_f.pack(pady=10)

s_f = Frame(application_window)
s_f.pack(pady=10)

l_f = Frame(application_window)
l_f.pack(pady = 10)

namel = Label(i_f, text="Name:")
namel.grid(row=0, column=0, padx=5, pady=5)
namee = Entry(i_f, width=50)
namee.grid(row=0, column=1, padx=5, pady=5)

emaill =Label(i_f, text="Email:")
emaill.grid(row=2, column=0, padx=5, pady=5)
emaile = Entry(i_f, width=50)
emaile.grid(row=2, column=1, padx=5, pady=5)

phonel = Label(i_f, text="Phone:")
phonel.grid(row=1, column=0, padx=5, pady=5)
phonee= Entry(i_f, width=50)
phonee.grid(row=1, column=1, padx=5, pady=5)

addressl = Label(i_f, text="Address:")
addressl.grid(row=3, column=0, padx=5, pady=5)
addresse = Entry(i_f, width=50)
addresse.grid(row=3, column=1, padx=5, pady=5)

add_b = Button(b_f , text ="Add Contact" , width = 10 , bg = "green" , command = add_c)
add_b.grid(row = 0 , column = 1 , pady = 5 , padx =5) 

del_b = Button(b_f , text="Delete Contact" , width = 12 , bg ="red" , command = delete_c)
del_b.grid(row =0 , column = 2 , pady = 10 , padx =5)

update_b = Button(b_f , text = "Update Contact" , width = 12 , bg = "brown" , command = update_c)
update_b.grid(row =0 , column = 3 , pady = 5 , padx = 10)    

clear_b = Button(b_f , text ="Clear Information" , width = 15 , bg = "lightpink" , command = clear_all)
clear_b.grid(row = 0 , column = 4 , pady = 5 , padx = 5)

searchl = Label(s_f , text ="Search Contact:")
searchl.grid(row = 0 , column = 0 , pady = 5 , padx = 5)
searche = Entry(s_f , width =50 )
searche.grid(row = 0 , column = 1 , pady = 5 , padx = 5)

search_b = Button(s_f , text = "Search Contact" , width = 12 , bg = "lightblue" , command = search_c)
search_b.grid(row =0 , column = 2 , pady =5 , padx =5)

showall_b = Button(s_f , text = "Show All Contants" , bg ="lightblue" , command = clear_search)
showall_b.grid(row =0 , column = 3 , pady = 5 , padx = 5 )

cl = Listbox(l_f, width=80, height=10 , bd = 5)
cl.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
cl.bind('<<ListboxSelect>>', view_c)

sb = Scrollbar(l_f)
sb.pack(side=RIGHT, fill=Y)

cl.config(yscrollcommand=sb.set)
sb.config(command=cl.yview)

application_window.mainloop()
