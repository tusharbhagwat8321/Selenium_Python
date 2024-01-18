from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH,"//input[@value='Male']")

li = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Movies':
        ele.click()



