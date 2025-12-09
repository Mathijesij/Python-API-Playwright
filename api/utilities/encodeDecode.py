# from cryptography.fernet import Fernet
#
# key = Fernet.generate_key()
# print(key.decode())

# from cryptography.fernet import Fernet
# import os
#
# key = os.getenv("SECRET_KEY").encode()
# cipher = Fernet(key)
#
# password = "Markey@2435".encode()
# token = cipher.encrypt(password)
# print(token.decode())

import os

print(os.getenv("SECRET_KEY"))
