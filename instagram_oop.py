
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from auto_data import username, password
import pickle
import requests



class InstagramBot():
    

    def __init__(self,username, password) -> None:

        self.username = username 
        self.password = password 
        self.main_page = "https://instagram.com/"

        #options
        options = webdriver.ChromeOptions()
        #options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

        #disable webdriver mode
        options.add_argument("--disable-blink-features=AutomationControlled")

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})


        self.driver = webdriver.Chrome(
             executable_path='/Users/denyszvarych/Desktop/silenium_project/chromedriver',
             options=options
        )


    def close_browser(self):

        self.driver.close()
        self.driver.quit()
    
    # def save_cookies(self):
        
    #     driver = self.driver

    #     pickle.dump(driver.get_cookies(), open('test_cookies', 'wb'))

    #     # for cookie in pickle.load(open('test_cookies', 'rb')):
    #     #         driver.add_cookie(cookie)

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
        time.sleep(7)
        #self.close_browser()


    def save_img(self, nickname):

        self.login()
        account_url  = 'https://instagram.com/' + nickname
        self.driver.get(account_url)

        time.sleep(2)

        img_src = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/div/div/span/img'
        account_img = self.driver.find_element(By.XPATH, img_src).get_attribute('src')


        get_img = requests.get(account_img)
        with open(f'{nickname}_img','wb') as img_file:
            img_file.write(get_img.content)
        
        self.close_browser()

    #sprawdza czy element instnieje na stronie

    def xpath_exists(self):

        driver = self.driver

        try:
            driver.find_element(By.XPATH, self.account_url)
            exists =  True
        except NoSuchElementException:
            exists = False

        return exists 
    


my_bot = InstagramBot(username, password)
my_bot.save_img('busterzy')
#my_bot.login()
#my_bot.close_browser()