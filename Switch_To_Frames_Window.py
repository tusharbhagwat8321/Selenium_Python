import selenium

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
driver.get("https://demo.automationtesting.in/Frames.html#google_vignette")
driver.maximize_window()

driver.switch_to.frame("singleframe")

text = driver.find_element(By.TAG_NAME,"input")
text.send_keys("This is text box")

driver.switch_to.default_content()
