import pathlib
import random
import string
import json

# Make the directory inside the PassMan
BASE_DIR = (pathlib.Path(__file__) / ".." / ".." ).resolve()
# Making the Passwords directory and the json file if it doesn't exist
pathlib.Path(BASE_DIR / "Passwords").mkdir(parents=True, exist_ok=True)

if not (pathlib.Path(BASE_DIR / "Passwords" / "test.json")).exists():
    with open(pathlib.Path(BASE_DIR / "Passwords" / "test.json").resolve(), "a+") as f:
        #f.write("Pass ={\n\t'Name': 'no',\n\t'password' : 'password'\n}")
        print()


def newPass():
    length = 16
    password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
    return password

