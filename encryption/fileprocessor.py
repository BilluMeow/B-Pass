from encryption.core import AESCipher
from pickle import load, dumps
from re import search
from os import remove

class Encryptor:
    def __init__(self) -> None:
        self.cipher = AESCipher()

    def encrypt(self, filename : str, password : str) -> bool:
        assert self.password_strength_checker(password) == True
        with open(filename, 'rb') as original_file:

            data = original_file.read()
            encrypted_data = self.cipher.encrypt(data, password)
            
            with open(filename[:filename.rfind('.')]+'_encrypted.dat', 'wb') as exporting_file:
                exporting_file.write(dumps(encrypted_data))
            
        remove(filename)


    def decrypt(self, filename : str, password : str) -> bool:
        assert self.password_strength_checker(password) == True
        with open(filename, 'rb') as original_file:

            encrypted_data = load(original_file)
            decrypted_data = self.cipher.decrypt(encrypted_data, password)
            
            with open(filename[:filename.rfind('_')]+'_decrypted.csv', 'wb') as exporting_file:
                exporting_file.write(decrypted_data)

    def password_strength_checker(self, password : str) -> bool:
        if len(password) < 21:
            raise Exception('Password too small')
        elif len(password) > 40:
            raise Exception('Password to big.')
        
        if not search("[a-z]", password):
            raise Exception('Password should contain atleast 1 small letter')

        if not search("[A-Z]", password):
            raise Exception('Password should contain atleast 1 capital letter')

        if not search("[0-9]", password):
            raise Exception('Password should contain atleast 1 number')

        if not search("[!@#$%^&*?~]", password):
            raise Exception('Password should contain atleast 1 special character')

        if search("[^!@#$%^&*?~0-9A-Za-z]", password):
            raise Exception('Password should not contain any of these : ()-_=+[]{/}\\;:\'\".,<>|`')

        return True

