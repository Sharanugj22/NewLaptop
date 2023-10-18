import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
time.sleep(2)

#driver.find_element(By.XPATH, "//select[@class='custom-select']").send_keys("Norway")
#driver.find_element(By.XPATH, "//select[@class='custom-select']/option[2]")

# select=Select(driver.find_element(By.XPATH, "//body/div[1]/div[3]/div[2]"))
# print(select)

sel=Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))
sel.select_by_index(2)
driver.sa
#screnshot........
#driver.save_screenshot(location+"\\ss.png")