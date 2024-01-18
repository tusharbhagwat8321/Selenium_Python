import time
import pyautogui
import self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
element_present=driver.find_element(By.ID,'imagesrc')
element_present.send_keys("C:/Users/tusha/Pictures/Screenshots/787663.png")



