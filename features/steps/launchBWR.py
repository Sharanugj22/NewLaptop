import time

from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#User below script for allure report and run on terminal
#behave -f allure_behave.formatter:AllureFormatter -o reports/ features
#allure serve reports/

@given('Launch browser')
def launcgBrowser(context):
    r_options = Options()
    r_options.add_experimental_option('detach', True)
    r_options.add_argument('--disable-notifications')
    context.driver=webdriver.Chrome(options=r_options)
    context.driver.maximize_window()


@when('Open NG site')
def openSite(context):
    context.driver.get("https://www.facebook.com/login/")
    time.sleep(5)

# @then('verify log present on home page')
# def verifyLogo(context):
#     print(context.driver.title)
#     status=context.driver.find_element(By.XPATH,"//img[@alt='Facebook']").is_displayed()
#     assert status is True

@when('Enter username "{user}" and password "{pwd}"')
def enterUsername(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@id='pass']").send_keys(pwd)
    context.driver.find_element(By.XPATH,"//button[@id='loginbutton']").click()
    time.sleep(20)

@when('Close browser')
def closeBrowser(context):
    print(context.driver.title)
    context.driver.close()