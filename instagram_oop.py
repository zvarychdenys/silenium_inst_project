
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from auto_data import username, password
import pickle
import requests

class InstagramBot():

    def __init__(self, username, password):

        self.username = username 
        self.password = password 
        self.main_page = "https://instagram.com/"

        #options
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (X11; CrOS x86_64 14816.131.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")

        #headless
        #options.headless = True


        self.driver = webdriver.Chrome(
             executable_path='/Users/denyszvarych/Desktop/silenium_project/chromedriver',
             options=options
        )


    def close_browser(self):

        self.driver.close()
        self.driver.quit()

    def login(self):

        driver = self.driver
        driver.get(self.main_page)
        
        # accept_all_cookies
        cookies = driver.find_element(By.CLASS_NAME, "aOOlW").click() 
        time.sleep(1)

        login_form = driver.find_element(By.NAME, 'username')
        login_form.send_keys(username)

        password_form = driver.find_element(By.NAME, 'password')
        password_form.send_keys(password)
        password_form.send_keys(Keys.ENTER)
        time.sleep(3)
        #self.close_browser()


    def save_img(self, nickname):

        self.login()
        account_url  = 'https://instagram.com/' + nickname
        self.driver.get(account_url)
        time.sleep(1)

        img_src = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/div/div/span/img'
        account_img = self.driver.find_element(By.XPATH, img_src).get_attribute('src')

        get_img = requests.get(account_img)
        with open(f'img_instagram/{nickname}.jpeg','wb') as img_file:
            img_file.write(get_img.content)
        

        self.close_browser()


#my_bot = InstagramBot(username, password)
#by_bot.save_img('zvarich87')
#my_bot.login()
#my_bot.close_browser()