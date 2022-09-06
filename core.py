# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

class AESCipher:

    def __init__(self) -> None:
        self.salt = b"8bea2d47c34340fb9bfb1faee56108844d78ece2c06d6e8cc8f4a0eae41a5984"

    def encrypt(self, plain_text : str, password : str) -> dict:
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = self.get_key(password)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
        }


    def decrypt(self, enc_dict : dict, password : str) -> str:
        # decode the dictionary entries from base64
        salt = b64decode(enc_dict['salt'])
        cipher_text = b64decode(enc_dict['cipher_text'])
        nonce = b64decode(enc_dict['nonce'])
        tag = b64decode(enc_dict['tag'])
        

        # generate the private key from the password and salt
        private_key = self.get_key(password)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted

    def get_key(self, password : str) -> str:
        return hashlib.scrypt(password.encode(), salt=self.salt, n=2**14, r=8, p=1, dklen=32)