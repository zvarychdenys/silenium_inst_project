from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from auto_data import username, password
import pickle


#options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1")

driver = webdriver.Chrome(
    executable_path='/Users/denyszvarych/Desktop/silenium_project/chromedriver',
    options=options)

url = 'https://instagram.com/'

text_username = 'den_zv03'
try:
    # driver.get(url)
    # cookies = driver.find_element(By.CLASS_NAME, "aOOlW").click() # accept_all_cookies
    # time.sleep(3)

    # login_form = driver.find_element(By.NAME, 'username')
    # login_form.send_keys(username)

    # password_form = driver.find_element(By.NAME, 'password')
    # password_form.send_keys(password)
    # password_form.send_keys(Keys.ENTER)
    # time.sleep(10)

    # # cookies   
    # pickle.dump(driver.get_cookies(), open(f'{username}_cookies', 'wb'))
    
    driver.get('https://instagram.com/' + text_username)

    for cookie in pickle.load(open(f'{username}_cookies', 'rb')):
        driver.add_cookie(cookie)
    
    driver.refresh()
    time.sleep(10)


except Exception as _ex: 
    print(_ex)
finally:
    driver.close()
    driver.quit()

    

