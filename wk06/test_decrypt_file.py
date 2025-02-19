import unittest
import os
import sqlite3
from unittest.mock import patch
import final_project
from cryptography.fernet import Fernet
def test_decrypt_file(self, mock_mb):

        test_file = "test_decrypt.txt"
        original_content = b"Hello, World!"
        with open(test_file, "wb") as f:
            f.write(original_content)
        key = final_project.encrypt_file(test_file, "")
        

        conn = sqlite3.connect(final_project.DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO locks (filepath, password, unlock_time) VALUES (?, ?, ?)",
                  (test_file, key, 0))  
        conn.commit()
        conn.close()
        

        final_project.decrypt_file(test_file, "")
        

        with open(test_file, "rb") as f:
            decrypted_content = f.read()
        self.assertEqual(decrypted_content, original_content)
        

        conn = sqlite3.connect(final_project.DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM locks WHERE filepath=?", (test_file,))
        self.assertIsNone(c.fetchone())
        conn.close()
        

        mock_mb.showinfo.assert_called_with("Success", "File has been decrypted!")
        

        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()