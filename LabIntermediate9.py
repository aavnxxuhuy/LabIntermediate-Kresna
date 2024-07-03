import mysql.connector
import tkinter as tk
import re
from tkinter import messagebox, ttk

class CrudTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.create_widgets()
        self.configure_grid()
        self.show_contacts()

        # Mengaitkan fungsi untuk menampilkan data terpilih dari Treeview ke Entry
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

    # Fungsi untuk menghubungkan ke sebuah database
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="db_inter"
        )

    def validate_phone_number(self, phone):
        # Validasi nomor telepon yang hanya berisi angka
        if re.match(r'^\d+$', phone):
            return True
        else:
            return False

    def validate_email(self, email):
        # Validasi format email
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return True
        else:
            return False

    # Fungsi Create
    def insert_contacts(self, nama, alamat, nomor_handphone, email):
        if not self.validate_phone_number(nomor_handphone):
            messagebox.showerror("Error", "Phone number must contain only digits.")
            return
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        db = self.connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO kontak (nama, alamat, nomor_handphone, email) VALUES (%s, %s, %s, %s)"
        val = (nama, alamat, nomor_handphone, email)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Info", "Contact created successfully")
        self.show_contacts()

    # Fungsi Retrieve
    def retrieve_contacts(self):
        db = self.connect_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kontak")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    # Fungsi Update
    def update_contact(self, contact_id, nama=None, alamat=None, nomor_handphone=None, email=None):
        if nomor_handphone and not self.validate_phone_number(nomor_handphone):
            messagebox.showerror("Error", "Phone number must contain only digits.")
            return
        if email and not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        db = self.connect_db()
        cursor = db.cursor()
        updates = []
        vals = []
        if nama:
            updates.append("nama = %s")
            vals.append(nama)
        if alamat:
            updates.append("alamat = %s")
            vals.append(alamat)
        if nomor_handphone:
            updates.append("nomor_handphone = %s")
            vals.append(nomor_handphone)
        if email:
            updates.append("email = %s")
            vals.append(email)

        sql = f"UPDATE kontak SET {', '.join(updates)} WHERE id = %s"
        vals.append(contact_id)
        cursor.execute(sql, vals)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Info", "Contact updated successfully")
        self.show_contacts()

    # Fungsi Delete
    def delete_contact(self, contact_id):
        db = self.connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM kontak WHERE id = %s"
        val = (contact_id,)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Info", "Contact deleted successfully")
        self.show_contacts()

    # Menampilkan Data
    def show_contacts(self):
        contacts = self.retrieve_contacts()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for contact in contacts:
            self.tree.insert("", "end", values=(contact['id'], contact['nama'], contact['alamat'], contact['nomor_handphone'], contact['email']))

    # Membuat Fungsi GUI
    def create_contact(self):
        self.insert_contacts(self.entry_name.get(), self.entry_address.get(), self.entry_phone.get(), self.entry_email.get())

    def update_selected_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            contact_id = self.tree.item(selected_item)["values"][0]
            self.update_contact(contact_id, self.entry_name.get(), self.entry_address.get(), self.entry_phone.get(), self.entry_email.get())

    def delete_selected_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            contact_id = self.tree.item(selected_item)["values"][0]
            self.delete_contact(contact_id)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            values = item["values"]
            self.entry_name.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_name.insert(0, values[1])  # Nama
            self.entry_address.insert(0, values[2])  # Alamat
            self.entry_phone.insert(0, values[3])  # Nomor Handphone
            self.entry_email.insert(0, values[4])  # Email

    # Membuat UI Tombol dan Listbox treview dan entry
    def create_widgets(self):
        padding = {'padx': 2, 'pady': 4}

        tk.Label(self.root, text="Name").grid(row=0, column=0, sticky="ew", **padding)
        tk.Label(self.root, text="Address").grid(row=1, column=0, sticky="ew", **padding)
        tk.Label(self.root, text="Phone").grid(row=2, column=0, sticky="ew", **padding)
        tk.Label(self.root, text="Email").grid(row=3, column=0, sticky="ew", **padding)

        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, columnspan=2, sticky="ew", **padding)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=1, column=1, columnspan=2, sticky="ew", **padding)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=2, column=1, columnspan=2, sticky="ew", **padding)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=3, column=1, columnspan=2, sticky="ew", **padding)

        tk.Button(self.root, text="Create", command=self.create_contact).grid(row=4, column=0, sticky="ew", **padding)
        tk.Button(self.root, text="Update", command=self.update_selected_contact).grid(row=4, column=1, sticky="ew", **padding)
        tk.Button(self.root, text="Delete", command=self.delete_selected_contact).grid(row=4, column=2, sticky="ew", **padding)
        tk.Button(self.root, text="Refresh", command=self.show_contacts).grid(row=5, column=0, columnspan=3, sticky="ew", **padding)

        columns = ("ID", "Name", "Address", "Phone", "Email")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")

        self.tree.grid(row=6, column=0, columnspan=3, sticky="nsew", **padding)

    # Membuat responsive UI
    def configure_grid(self):
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

root = tk.Tk()
app = CrudTkinter(root)
root.mainloop()
