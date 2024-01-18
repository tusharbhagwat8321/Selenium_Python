from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.get("https://demo.automationtesting.in/Index.html")
email=driver.find_element(By.ID,'email')
email.send_keys("tushar@gmail.com")
driver.find_element(By.ID,"enterimg").click()