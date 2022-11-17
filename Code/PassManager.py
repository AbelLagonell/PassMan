import os.path

BASE_DIR = os.path.dirname(os.path.realpath("PassManager.py"))
BASE_DIR = '{}/PassMan'.format(BASE_DIR)
JSON_DIR = '{}/Passwords/test.json'.format(BASE_DIR)  

with open(JSON_DIR, "w+") as f:
    print("hello")
