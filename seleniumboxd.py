import time
import sqlite3
from seleniumboxd_helper import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sql = sqlite3.connect("users.db", timeout=10)
cursor = sql.cursor()
# cursor.execute("CREATE TABLE user(discord_handle, username, password)")
# cursor.execute


driver = webdriver.Chrome(ChromeDriverManager().install()) 
wait = WebDriverWait(driver,10)

    
driver.get('https://letterboxd.com/sign-in/')
 
user = get_login(cursor,"62274677#1025")
sign_in(driver, user["username"], user["password"])

movie = "Barbarian"
add_movie(driver, sql, wait, movie)




    
    
    
terminate(driver,sql)