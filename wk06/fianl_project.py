import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import sqlite3
import threading
import base64
import random
import string

DB_FILE = "lockbox.db"   #db for storing passwords securely


def init_db():                              #initialize db
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS locks (
            id INTEGER PRIMARY KEY,
            filepath TEXT,
            password TEXT,
            unlock_time INTEGER
        )
    """)
    conn.commit()
    conn.close()


def generate_key(): #this class generates encryption key
    return Fernet.generate_key().decode()  # Correctly formatted key


def encrypt_file(filepath, password):    #encrypfile/folder using AES encryption
    key = generate_key().encode()  #this ensures it’s in bytes
    cipher = Fernet(key)

    with open(filepath, "rb") as f:
        encrypted_data = cipher.encrypt(f.read())

    with open(filepath, "wb") as f:
        f.write(encrypted_data)

    return key.decode()  # Return key for storage


def decrypt_file(filepath, password):    #this function decrypts the file/folder when time expires
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT password, unlock_time FROM locks WHERE filepath=?", (filepath,))
    result = c.fetchone()
    
    if not result:
        messagebox.showerror("Error", "File not found in database.")
        return
    
    stored_password, unlock_time = result

    if time.time() < unlock_time:      #this checks if time has expired
        messagebox.showwarning("Wait", "The timer has not expired yet!")
        return

    cipher = Fernet(stored_password.encode())
    with open(filepath, "rb") as f:
        decrypted_data = cipher.decrypt(f.read())

    with open(filepath, "wb") as f:
        f.write(decrypted_data)


    c.execute("DELETE FROM locks WHERE filepath=?", (filepath,))#removes record from database.
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "File has been decrypted!")


def generate_random_password():#generate a random password
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def lock_file(filepath, user_password, duration):   #locks the file/folder
    password = user_password if user_password else generate_random_password()
    encrypted_key = encrypt_file(filepath, password)

    unlock_time = time.time() + duration


    conn = sqlite3.connect(DB_FILE) #stores in database
    c = conn.cursor()
    c.execute("INSERT INTO locks (filepath, password, unlock_time) VALUES (?, ?, ?)",
              (filepath, encrypted_key, unlock_time))
    conn.commit()
    conn.close()

    messagebox.showinfo("Locked", f"File locked successfully! Unlocks in {duration // 60} minutes.")


    threading.Thread(target=unlock_timer, args=(filepath, unlock_time)).start()     #starts countdown in a separate thread


def unlock_timer(filepath, unlock_time):  #timer function
    while time.time() < unlock_time:
        time.sleep(10)
    messagebox.showinfo("Unlocked", f"The file {filepath} can now be unlocked.")

def open_gui():     #gui function
    def select_file():
        file_path = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

    def lock():
        filepath = file_entry.get()
        password = password_entry.get()
        try:
            duration = int(time_entry.get()) * 60  #cvonvert to seconds
        except ValueError:
            messagebox.showerror("Error", "Invalid time duration.")
            return

        if not os.path.exists(filepath):
            messagebox.showerror("Error", "File does not exist.")
            return

        lock_file(filepath, password, duration)

    def unlock():
        filepath = file_entry.get()
        if not os.path.exists(filepath):
            messagebox.showerror("Error", "File does not exist.")
            return

        decrypt_file(filepath, "")

    
    root = tk.Tk() #sets up gui
    root.title("LockBox")
    root.geometry("400x300")

    tk.Label(root, text="Select File to Lock:").pack()
    file_entry = tk.Entry(root, width=40)
    file_entry.pack()
    tk.Button(root, text="Browse", command=select_file).pack()

    tk.Label(root, text="Set Unlock Duration (minutes):").pack()
    time_entry = tk.Entry(root, width=10)
    time_entry.pack()

    tk.Label(root, text="(Optional) Set Custom Password:").pack()
    password_entry = tk.Entry(root, width=20, show="*")
    password_entry.pack()

    tk.Button(root, text="Lock File", command=lock).pack(pady=10)
    tk.Button(root, text="Unlock File", command=unlock).pack()

    root.mainloop()


if __name__ == "__main__":   #initialize and run the program.
    init_db()
    open_gui()
