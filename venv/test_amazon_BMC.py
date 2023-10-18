import os
from telnetlib import EC
import openpyxl
import XLUtils

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# location = os.getcwd()
# r_options = Options()
# r_options.add_experimental_option('detach', True)
# r_options.add_argument('--disable-notifications')
# driver = webdriver.Chrome(options=r_options)
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
path = "C://Users//DELL//Desktop//Test.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")
cols = XLUtils.getColunmCount(path, "Sheet1")

for r in range(2, rows + 1):
    username = XLUtils.redData(path, "Sheet1", r, 1)
    password = XLUtils.redData(path, "Sheet1", r, 2)

    ss=driver.find_element(By.XPATH, "//*[@id='input']").send_keys(username)
    ss.submit()
    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@id='loginbutton']").click()
    driver.implicitly_wait(15)

    if driver.title == 'Facebook':
        print("TC is Passed")
        XLUtils.writedata(path, "Sheet1", r, 3, "Test is passed")

    else:
        print("TC is Failed")
        XLUtils.writedata(path, "Sheet1", r, 3, "Test is failed")