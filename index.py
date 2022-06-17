import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests

# with open("proxy.txt") as f:
#     lines = f.readlines()
# PROXY = random.choice(lines)

low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
a = []


options = uc.ChromeOptions()
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.add_argument("--window-size=1920,1080")
driver = uc.Chrome(options=options)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
timez = int(time.time())+30
print("rawr")
a = True
driver.get('https://glitch.com/edit/#!/remix/chipped-aged-clavicle')
timez = int(time.time())+120
while a==True:
    if(driver.current_url.startswith("https://glitch.com/edit/#!/remix/chipped-aged-clavicle")):
        time.sleep(0.2)
        if(timez<int(time.time())):
            a = False
            driver.close()


    else:
        a = False
        val = driver.current_url
        val = val.replace("https://glitch.com/edit/#!/", "")
        val = val.replace("?path=README.md%3A1%3A0", "")
        val = "https://"+val+".glitch.me/"
        print(val)
        payload = "test="+val
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
            }
        response = requests.request("POST", "https://RealFoolhardyAddin.idotmastera.repl.co/rawr", data=payload, headers=headers)
        print(response)
        driver.close()





#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").click()
#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").send_keys(namerepl)
