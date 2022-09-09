from core import AESCipher
import pickle

import json

class Encryptor:
    def __init__(self) -> None:
        self.cipher = AESCipher()

    def encrypt(self, filename : str, password : str) -> bool:
        with open(filename, 'rb') as original_file:

            data = original_file.read()
            encrypted_data = self.cipher.encrypt(data, password)
            
            with open(filename[:filename.rfind('.')]+'_encrypted.dat', 'wb') as exporting_file:
                exporting_file.write(pickle.dumps(encrypted_data))


    def decrypt(self, filename : str, password : str) -> bool:
        with open(filename, 'rb') as original_file:

            encrypted_data = pickle.load(original_file)
            decrypted_data = self.cipher.decrypt(encrypted_data, password)
            
            with open(filename[:filename.rfind('_')]+'_decrypted.csv', 'wb') as exporting_file:
                exporting_file.write(decrypted_data)

    def password_strength_checker(self, password : str) -> bool:

        if len(password) < 21:
            raise Exception('Password too small')

        return True

