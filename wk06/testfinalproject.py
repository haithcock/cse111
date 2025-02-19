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

class testfinalproject(unittest.TestCase):
    def setUp(self):
        final_project.DB_FILE = "test_lockbox.db"
        final_project.init_db()
    
    def teardown(self):
        if os.path.exists(final_project.DB_FILE):
            os.remove(final_project.DB_FILE)

    def test_generate_key(self):
        key = final_project.generate_key()
        self.assertIsInstance(key, str)
        self.assertEqual(len(key), 44)
        try:
            Fernet(key.encode())
        except Exception as e:
            self.fail(f"Invalid key generated: {e}")


if __name__ == "__main__":
    unittest.main()