from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://www.redbus.in/")
driver.implicitly_wait(3)
driver.maximize_window()

select_date = "20-Dec=2022"

dates = select_date.split("-")

driver.find_element(By.ID,"onwardCal").click()

td = driver.find_elements(By.XPATH,"//div[@id='rb-calender_onward_cal']//td")

for ele in td:
    if ele.text == dates[0]:
        ele.click()
        break