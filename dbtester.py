
import sqlite3
from seleniumboxd_helper import *


sql = sqlite3.connect("users.db")
cursor = sql.cursor()

user = get_login(cursor,"62274677#1025")
print(user)