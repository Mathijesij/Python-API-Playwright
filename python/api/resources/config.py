import configparser
from pathlib import Path

config_path = r"C:\Users\MathijesiJohnbritto\PycharmProjects\demo\python\api\config\config.ini"

config = configparser.ConfigParser()
read_files = config.read(config_path)

if not read_files:
    raise FileNotFoundError(f"Config file not found at {config_path}")

base_url = config["API"]["base_url"]

productlist = config["EndPoints"]["productlist"]
verifylogin = config["EndPoints"]["verifylogin"]
createaccount = config["EndPoints"]["createaccount"]
brandlist = config["EndPoints"]["brandlist"]
searchproduct = config["EndPoints"]["searchproduct"]
updateAccount = config["EndPoints"]["updateAccount"]
getUserDetailByEmail = config["EndPoints"]["getUserDetailByEmail"]
deleteAccount = config["EndPoints"]["deleteAccount"]

def get_api_base_url():
    return base_url
