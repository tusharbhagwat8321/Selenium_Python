from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

parent = driver.current_window_handle
print(parent)

driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()

windows = driver.window_handles


for win in windows:
    if win !=parent:
        driver.switch_to.window(win)


driver.find_element(By.XPATH,"//span[contains(text(),'Downloads')]").click()
driver.close()

driver.switch_to.window(parent)
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()

driver.quit()
