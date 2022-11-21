# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import scrypt

class AESCipher:

    def __init__(self) -> None:
        pass

    def encrypt(self, plain_text : str, password : str) -> dict:
        # generate key and salt
        private_key, salt = self.generate_key(password)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(str(plain_text, 'utf-8'), 'utf-8'))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8'),
            'salt' : b64encode(salt).decode('utf-8'),
            'nonce' : b64encode(cipher_config.nonce).decode('utf-8')
        }


    def decrypt(self, cypher_text : dict, password : str) -> str:
        # decode the dictionary entries from base64
        cipher_text = b64decode(cypher_text['cipher_text'])
        salt = b64decode(cypher_text['salt'])
        tag = b64decode(cypher_text['tag'])
        nonce = b64decode(cypher_text['nonce'])
        

        # generate the private key from the password and salt
        private_key, _ = self.generate_key(password, salt=salt)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted

    def generate_key(self, password : str, salt=None) -> str:
        if salt is None:
            salt = self.generate_salt()

        return (scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32), salt)

    def generate_salt(self) -> bytes:
        return get_random_bytes(AES.block_size)
