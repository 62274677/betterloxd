import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def dict_from_row(description,values):
    keys = []
    for col in description:
        keys.append(col[0])
    return dict(zip(keys, values))

def get_login(cursor, discord_handle):
    execute_string = "select * from user where discord_handle='{}'".format(discord_handle)
    # print(execute_string)
    res = cursor.execute(execute_string).fetchall()
    # print(type(ress))
    # print(cursor.description)
    user_info = dict_from_row(cursor.description, res[0])
    return user_info

def sign_in(driver, user, password):
    user_input = driver.find_element_by_name("username")
    user_input.send_keys(user)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)
    pass
    
def add_movie(driver, sql, wait, movie):
    driver.find_elements_by_class_name("button-green")[0].click()
    # print(type(signin_button))
    # time.sleep(1)
    add_button = wait.until(EC.element_to_be_clickable((By.ID, 'add-new-button')))
    add_button.click()
    wait.until(EC.presence_of_element_located((By.ID,'frm-film-name')))
    time.sleep(1)
    film_input = driver.find_elements_by_id('frm-film-name')[0]
    film_input.send_keys(movie)
    time.sleep(2)
    film_input.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        submit = wait.until(EC.element_to_be_clickable((By.ID, 'diary-entry-submit-button')))
        submit.click()
    except:
        terminate(driver,sql)
        
    time.sleep(1)    
def terminate(driver,sql):
    sql.close()
    driver.close()
    pass

def initiate_driver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
    chromeOptions.add_argument("--no-sandbox") 
    chromeOptions.add_argument("--disable-setuid-sandbox") 

    chromeOptions.add_argument("--remote-debugging-port=9222")  # this

    chromeOptions.add_argument("--disable-dev-shm-using") 
    chromeOptions.add_argument("--disable-extensions") 
    chromeOptions.add_argument("--disable-gpu") 
    chromeOptions.add_argument("start-maximized") 
    chromeOptions.add_argument("disable-infobars")
    chromeOptions.add_argument(r"user-data-dir=\.\\cookies\\test") 

    return webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chromeOptions) 
    