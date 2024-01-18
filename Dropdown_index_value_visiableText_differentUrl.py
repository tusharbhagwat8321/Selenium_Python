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
driver.maximize_window()

select_web = driver.find_elements(By.ID,'Skills')

sel = Select(select_web[0])

sel.select_by_index(5)

sel.select_by_value('Configuration')

sel.select_by_visible_text('Design')

driver.get("https://www.google.com/")

driver.back()

driver.refresh()

driver.forward()

driver.quit()