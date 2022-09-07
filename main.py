
from fileprocessor import Encryptor

def main():
    password = input("Password: ")

    encryptor = Encryptor()

    # First let us encrypt secret message
    encrypted = encryptor.encrypt("testing/google.csv", password)
    '''print(encrypted['cipher_text'])

    # Let us decrypt using our original password
    decrypted = encryptor.decrypt(encrypted, password)
    print(bytes.decode(decrypted))'''

main()