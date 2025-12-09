import configparser
import os
from cryptography.fernet import Fernet
from pathlib import Path

config_path = Path(__file__).parent / "utilities" / "config.ini"

config = configparser.ConfigParser()

config.read(config_path)

def get_api_base_url():
    return config["API"]["base_url"]

key = os.getenv("SECRET_KEY").encode()
cipher = Fernet(key)

def decrypt(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

def get_credentials():
    email = config["Credentials"]["email"]
    enc_pass = config["Credentials"]["password"]
    password = decrypt(enc_pass)
    return {"email": email, "password": password}

def get_new_user_payload():
    user = config["NewUser"]
    data = {k: user[k] for k in user}
    data["password"] = decrypt(user["password"])
    return data

def get_search_product():
    return dict(config['searchProduct'])

def get_valid_login():
    email = config["ValidLogin"]["email"]
    enc_pass = config["ValidLogin"]["password"]
    password = decrypt(enc_pass)
    return {"email": email, "password": password}

def get_password():
    enc_pass = config["withoutEmail"]["password"]
    password = decrypt(enc_pass)
    return {"password": password}

def get_update_user():
    user = config["UpdateUser"]
    data = {k: user[k] for k in user}
    data["password"] = decrypt(user["password"])
    return data

def get_user_by_email():
    return dict(config['getUser'])

def get_delete_user():
    email = config["deleteAccount"]["email"]
    enc_pass = config["deleteAccount"]["password"]
    password = decrypt(enc_pass)
    return {"email": email, "password": password}



