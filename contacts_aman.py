import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []
        
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#E1E1E1")
        self.style.configure("TButton", background="#4CAF50", foreground="white")
        self.style.configure("TLabel", background="#E1E1E1")
        self.style.configure("TEntry", background="white")
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        
        self.label_name = ttk.Label(self.frame, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.entry_name = ttk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_phone = ttk.Label(self.frame, text="Phone Number:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        self.entry_phone = ttk.Entry(self.frame)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_email = ttk.Label(self.frame, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        self.entry_email = ttk.Entry(self.frame)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)
        
        self.label_address = ttk.Label(self.frame, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        self.entry_address = ttk.Entry(self.frame)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)
        
        self.button_add = ttk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, padx=5, pady=5, sticky="W")
        
        self.button_view = ttk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=4, column=1, padx=5, pady=5, sticky="E")
        
        self.label_search = ttk.Label(self.frame, text="Search:")
        self.label_search.grid(row=5, column=0, padx=5, pady=5, sticky="W")
        self.entry_search = ttk.Entry(self.frame)
        self.entry_search.grid(row=5, column=1, padx=5, pady=5)
        
        self.button_search = ttk.Button(self.frame, text="Search", command=self.search_contact)
        self.button_search.grid(row=6, column=0, padx=5, pady=5, sticky="W")
        
        self.button_update = ttk.Button(self.frame, text="Update", command=self.update_contact)
        self.button_update.grid(row=6, column=1, padx=5, pady=5, sticky="E")
        
        self.button_delete = ttk.Button(self.frame, text="Delete", command=self.delete_contact)
        self.button_delete.grid(row=7, column=0, padx=5, pady=5, sticky="W")
        
    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        
        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")
        
        self.clear_entries()
        
    def view_contacts(self):
        if len(self.contacts) == 0:
            messagebox.showinfo("No Contacts", "No contacts found.")
        else:
            contact_list = "Contact List:\n"
            for contact in self.contacts:
                contact_list += f"Name: {contact.name}, Phone Number: {contact.phone_number}\n"
            messagebox.showinfo("Contacts", contact_list)
        
    def search_contact(self):
        search_term = self.entry_search.get()
        found_contacts = []
        
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        
        if len(found_contacts) == 0:
            messagebox.showinfo("No Contacts", "No matching contacts found.")
        else:
            contact_list = "Matching Contacts:\n"
            for contact in found_contacts:
                contact_list += f"Name: {contact.name}, Phone Number: {contact.phone_number}\n"
            messagebox.showinfo("Matching Contacts", contact_list)
        
    def update_contact(self):
        search_term = self.entry_search.get()
        found_contacts = []
        
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        
        if len(found_contacts) == 0:
            messagebox.showinfo("No Contacts", "No matching contacts found.")
        else:
            contact_list = "Matching Contacts:\n"
            for contact in found_contacts:
                contact_list += f"Name: {contact.name}, Phone Number: {contact.phone_number}\n"
            choice = messagebox.askquestion("Update Contact", contact_list + "Do you want to update this contact?")
            
            if choice == "yes":
                for contact in found_contacts:
                    if search_term.lower() == contact.name.lower() or search_term == contact.phone_number:
                        new_name = self.entry_name.get()
                        new_phone_number = self.entry_phone.get()
                        new_email = self.entry_email.get()
                        new_address = self.entry_address.get()
                        
                        if new_name:
                            contact.name = new_name
                        if new_phone_number:
                            contact.phone_number = new_phone_number
                        if new_email:
                            contact.email = new_email
                        if new_address:
                            contact.address = new_address
                        
                        messagebox.showinfo("Success", "Contact updated successfully!")
                        break
        
        self.clear_entries()
        
    def delete_contact(self):
        search_term = self.entry_search.get()
        found_contacts = []
        
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        
        if len(found_contacts) == 0:
            messagebox.showinfo("No Contacts", "No matching contacts found.")
        else:
            contact_list = "Matching Contacts:\n"
            for contact in found_contacts:
                contact_list += f"Name: {contact.name}, Phone Number: {contact.phone_number}\n"
            choice = messagebox.askquestion("Delete Contact", contact_list + "Do you want to delete this contact?")
            
            if choice == "yes":
                for contact in found_contacts:
                    self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
        
        self.clear_entries()
        
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

root = tk.Tk()
contact_book = ContactBookGUI(root)
root.mainloop()
