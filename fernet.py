# Cifrado Fernet

from cryptography.fernet import Fernet

clave = Fernet.generate_key()

f = Fernet(clave)

print(clave)

token = f.encrypt(b'te quiero sofi aunque tengas esmalte emo p')

print(token)

des = f.decrypt(token)

print(des)
