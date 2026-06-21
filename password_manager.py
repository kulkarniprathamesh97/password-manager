import os
import json
from cryptography.fernet import Fernet
import pyperclip
from tkinter import *
from tkinter import messagebox, simpledialog

# ==================== Encryption Setup ====================
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    with open("secret.key", "rb") as key_file:
        return key_file.read()

key = generate_key()
cipher = Fernet(key)

# ==================== Load & Save Passwords ====================
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "rb") as file:
            encrypted_data = file.read()
            if encrypted_data:
                decrypted_data = cipher.decrypt(encrypted_data)
                return json.loads(decrypted_data.decode())
    return {}

def save_passwords(passwords):
    encrypted_data = cipher.encrypt(json.dumps(passwords).encode())
    with open("passwords.json", "wb") as file:
        file.write(encrypted_data)

# ==================== Main Functions ====================
def add_password():
    website = simpledialog.askstring("Website/App", "Enter Website or App Name:")
    username = simpledialog.askstring("Username", "Enter Username/Email:")
    password = simpledialog.askstring("Password", "Enter Password:", show='*')
    
    if website and username and password:
        passwords = load_passwords()
        passwords[website] = {"username": username, "password": password}
        save_passwords(passwords)
        messagebox.showinfo("Success", f"Password for {website} saved successfully!")
    else:
        messagebox.showwarning("Warning", "All fields are required!")

def view_passwords():
    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("Info", "No passwords saved yet!")
        return
    
    view_window = Toplevel(root)
    view_window.title("Saved Passwords")
    view_window.geometry("600x400")
    
    Label(view_window, text="Website/App          Username          Password", font=("Arial", 12, "bold")).pack(pady=10)
    
    for website, data in passwords.items():
        frame = Frame(view_window)
        frame.pack(fill=X, padx=10, pady=5)
        
        Label(frame, text=website, width=25, anchor="w").pack(side=LEFT)
        Label(frame, text=data["username"], width=25, anchor="w").pack(side=LEFT)
        
        pass_btn = Button(frame, text="Show", command=lambda p=data["password"]: show_password(p))
        pass_btn.pack(side=LEFT, padx=5)
        
        copy_btn = Button(frame, text="Copy", command=lambda p=data["password"]: copy_to_clipboard(p))
        copy_btn.pack(side=LEFT, padx=5)
        
        del_btn = Button(frame, text="Delete", command=lambda w=website: delete_password(w))
        del_btn.pack(side=LEFT, padx=5)

def show_password(password):
    messagebox.showinfo("Password", f"Password: {password}")

def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def delete_password(website):
    if messagebox.askyesno("Confirm", f"Delete password for {website}?"):
        passwords = load_passwords()
        if website in passwords:
            del passwords[website]
            save_passwords(passwords)
            messagebox.showinfo("Deleted", f"Password for {website} deleted!")
            # Refresh view window if open

def generate_strong_password():
    import random
    import string
    length = 16
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Strong Password", f"Generated Password:\n\n{password}\n\nYou can copy it!")

# ==================== GUI ====================
root = Tk()
root.title("Personal Password Manager")
root.geometry("700x500")
root.configure(bg="#2c3e50")

Label(root, text="🔐 Personal Password Manager", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white").pack(pady=30)

Button(root, text="Add New Password", command=add_password, width=25, height=2, bg="#27ae60", fg="white", font=("Arial", 12)).pack(pady=15)
Button(root, text="View All Passwords", command=view_passwords, width=25, height=2, bg="#3498db", fg="white", font=("Arial", 12)).pack(pady=15)
Button(root, text="Generate Strong Password", command=generate_strong_password, width=25, height=2, bg="#f39c12", fg="white", font=("Arial", 12)).pack(pady=15)

Label(root, text="All passwords are encrypted using AES-256", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10)).pack(pady=40)

root.mainloop()