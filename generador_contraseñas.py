import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
from cryptography.fernet import Fernet
import base64
import os


class PasswordManager:
    def __init__(self, root, key):
        self.passwords = {}
        self.key = key
        self.root = root
        self.load_passwords()
        self.show_password_flag = False
        self.draw_gui()

    def load_passwords(self):
        try:
            with open('passwords.json', 'r') as file:
                encrypted_passwords = file.read()
            f = Fernet(self.key)
            decrypted_passwords = f.decrypt(encrypted_passwords.encode()).decode()
            self.passwords = json.loads(decrypted_passwords)
        except (FileNotFoundError, ValueError):
            self.passwords = {}

    def save_passwords(self):
        f = Fernet(self.key)
        encrypted_passwords = f.encrypt(json.dumps(self.passwords).encode()).decode()
        with open('passwords.json', 'w') as file:
            file.write(encrypted_passwords)

    def add_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.passwords[service] = {
            'username': username,
            'password': password
        }
        self.save_passwords()
        self.list_passwords()

    def delete_password(self):
        service = self.service_entry.get()
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            self.list_passwords()

    def list_passwords(self):
        self.passwords_list.delete(0, tk.END)
        for service in self.passwords:
            self.passwords_list.insert(tk.END, service)

    def show_password(self, event):
        try:
            service = self.passwords_list.get(self.passwords_list.curselection())
            password_data = self.passwords[service]
            self.service_entry.delete(0, tk.END)
            self.service_entry.insert(0, service)
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, password_data['username'])
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password_data['password'])
        except tk.TclError:
            pass

    def search_password(self):
        search_term = self.search_entry.get()
        for service in self.passwords:
            if search_term.lower() in service.lower():
                self.passwords_list.selection_clear(0, tk.END)
                self.passwords_list.activate(self.passwords_list.get(0, tk.END).index(service))
                self.passwords_list.selection_set(self.passwords_list.get(0, tk.END).index(service))

    def change_master_password(self):
        old_password = simpledialog.askstring("Old Master Password", "Enter old master password:", show='*', parent=self.root)
        if old_password == self.key.decode():
            new_password = simpledialog.askstring("New Master Password", "Enter new master password:", show='*', parent=self.root)
            self.key = base64.urlsafe_b64encode(new_password.encode().ljust(32)[:32])
            self.save_passwords()

    def show_hide_password(self):
        if self.show_password_flag:
            self.password_entry.configure(show="*")
            self.show_password_flag = False
        else:
            self.password_entry.configure(show="")
            self.show_password_flag = True

    def draw_gui(self):
        self.root.title("Password Manager")

        entry_frame = ttk.Frame(self.root)
        entry_frame.pack(side=tk.TOP)

        self.service_label = ttk.Label(entry_frame, text="Service")
        self.service_label.grid(row=0, column=0)
        self.service_entry = ttk.Entry(entry_frame)
        self.service_entry.grid(row=0, column=1)

        self.username_label = ttk.Label(entry_frame, text="Username")
        self.username_label.grid(row=1, column=0)
        self.username_entry = ttk.Entry(entry_frame)
        self.username_entry.grid(row=1, column=1)

        self.password_label = ttk.Label(entry_frame, text="Password")
        self.password_label.grid(row=2, column=0)
        self.password_entry = ttk.Entry(entry_frame, show="*")
        self.password_entry.grid(row=2, column=1)

        self.show_password_button = ttk.Button(entry_frame, text="Show Password", command=self.show_hide_password)
        self.show_password_button.grid(row=2, column=2)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(side=tk.TOP)

        self.add_button = ttk.Button(button_frame, text="Add Password", command=self.add_password)
        self.add_button.grid(row=0, column=0)
        self.delete_button = ttk.Button(button_frame, text="Delete Password", command=self.delete_password)
        self.delete_button.grid(row=0, column=1)
        self.change_password_button = ttk.Button(button_frame, text="Change Master Password", command=self.change_master_password)
        self.change_password_button.grid(row=0, column=2)

        self.search_label = ttk.Label(button_frame, text="Search")
        self.search_label.grid(row=1, column=0)
        self.search_entry = ttk.Entry(button_frame)
        self.search_entry.grid(row=1, column=1)
        self.search_button = ttk.Button(button_frame, text="Search Password", command=self.search_password)
        self.search_button.grid(row=1, column=2)

        self.passwords_list = tk.Listbox(self.root)
        self.passwords_list.bind('<<ListboxSelect>>', self.show_password)
        self.passwords_list.pack(side=tk.TOP)

        self.list_passwords()

if __name__ == '__main__':
    root = tk.Tk()
    master_key = '123'
    master_key = master_key.encode()
    key = base64.urlsafe_b64encode(master_key.ljust(32)[:32])
    password_manager = PasswordManager(root, key)
    root.mainloop()
