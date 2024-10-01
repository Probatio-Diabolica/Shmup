from cryptography.fernet import Fernet

key=Fernet.generate_key()
f=Fernet(key)

with open('Settings.conf','rb') as opening:
    encrypted=opening.read()

def encrypt():...
# def decrypt():...

def decrypt():
    
    encrypt()


