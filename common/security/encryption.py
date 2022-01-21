from cryptography.fernet import Fernet
from settings import Encryption

def encrypt(message):
    fernet = Fernet(Encryption.key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decrypt(encMessage):
    fernet = Fernet(Encryption.key)
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage