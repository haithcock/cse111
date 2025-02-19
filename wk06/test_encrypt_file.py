import unittest
import os
from cryptography.fernet import Fernet
import final_project

class TestEncryptFile(unittest.TestCase):
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