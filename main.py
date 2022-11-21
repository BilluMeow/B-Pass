
from encryption.fileprocessor import Encryptor

def main():
    filename = input("Filename: ")
    password = input("Password: ")
    
    encryptor = Encryptor()

    # First let us encrypt secret message
    print("Do you want to Encrypt (Y) ? ==> ")
    if input()[0] == 'Y':
        encryptor.encrypt(filename, password)
    else:
        encryptor.decrypt(filename, password)

main()