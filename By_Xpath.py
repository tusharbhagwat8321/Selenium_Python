from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,'(//input[@type="text"])[1]').send_keys("Tushar")
driver.find_element(By.XPATH,'(//input[@type="text"])[2]').send_keys("Bhagwat")
driver.find_element(By.XPATH,'//textarea[@rows=3]').send_keys("At.Malewadi Tal.Daund Dist.Pune")
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("tusharbhagwat160@gmail.com")

