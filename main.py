
from encryption.fileprocessor import Encryptor

def main():
    password = input("Password: ")

    encryptor = Encryptor()

    # First let us encrypt secret message
    encryptor.encrypt("testing/fortio.txt", password)
    encryptor.decrypt("testing/fortio_encrypted.dat", password)

main()