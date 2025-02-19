import unittest
import os
import sqlite3
from unittest.mock import patch
import final_project.py
from final_project.py import lock_file, unlock_timer, open_gui
from tkinter import messagebox
from tkinter import filedialog
import time
import tkinter as tk
from cryptography.fernet import Fernet

def test_encrypt_file(self):
 
    test_file = "test_encrypt.txt"
    original_content = b"Hello, World!"
    with open(test_file, "wb") as f:
        f.write(original_content)

    key = final_project.encrypt_file(test_file, "dummy_password")
    
    with open(test_file, "rb") as f:
        encrypted_content = f.read()
    self.assertNotEqual(encrypted_content, original_content)
    

    cipher = Fernet(key.encode())
    decrypted_content = cipher.decrypt(encrypted_content)
    self.assertEqual(decrypted_content, original_content)
    

    os.remove(test_file)

if __name__ == "__main__":
    unittest.main()