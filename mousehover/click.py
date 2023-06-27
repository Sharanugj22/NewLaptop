import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
location=os.getcwd()
r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
name=driver.find_element(By.XPATH,"//input[@id='name']")
act=ActionChains(driver)
name=act.move_to_element(name).click().perform()
act.send_keys("12f").perform()
time.sleep(5)

#screnshot........
#driver.save_screenshot(location+"\\ss.png")