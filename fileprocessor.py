from core import AESCipher
from hashlib import scrypt
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

import json

class Encryptor:
    def __init__(self) -> None:
        self.cipher = AESCipher()

    def encrypt(self, filename : str, password : str) -> bool:
        with open(filename, 'rb') as original_file:

            data = original_file.read()
            private_key = self.get_key(password)
            encrypted_data = self.cipher.encrypt(data, private_key)
            
            with open(filename[:filename.rfind('.')]+'_encrypted.dat', 'w') as exporting_file:
                encrypted_data_json = json.dumps(encrypted_data)
                exporting_file.write(encrypted_data_json)


    def decrypt(self) -> bool:
        pass

    def get_key(self, password : str, salt=None) -> str:
        if salt is None:
            salt = self.generate_salt()

        return scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    def generate_salt(self) -> bytes:
        return get_random_bytes(AES.block_size)
