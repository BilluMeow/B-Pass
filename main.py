
from core import AESCipher

def main():
    password = input("Password: ")

    AES = AESCipher()

    # First let us encrypt secret message
    encrypted = AES.encrypt("My name is Abeer and abeer is a good boy now thats good", password)
    print(encrypted['cipher_text'])

    # Let us decrypt using our original password
    decrypted = AES.decrypt(encrypted, password)
    print(bytes.decode(decrypted))

main()