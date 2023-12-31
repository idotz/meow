import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
import pyautogui
from PIL import Image

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
driver.get('https://youtu.be/U3oEvGpHRz8')
time.sleep(30)
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Send screenshot to Discord webhook
with open("screenshot.png", "rb") as img:
   response = requests.post(
       'https://canary.discord.com/api/webhooks/1190831794157789194/7woA16J43vhLVfh9sXAv2390jfJxTB_OGe3fWOlweP_F5b7-XFkAcSO2Z3XPut3m0lrb',
       files={'file': img}
   )

# Check if the request was successful
if response.status_code == 200:
   print("Screenshot sent successfully.")
else:
   print("Failed to send screenshot.")






#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").click()
#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").send_keys(namerepl)
