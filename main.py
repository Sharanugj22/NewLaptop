#Checkbox
import time

# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# r_options = Options()
# r_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=r_options)
# driver.get("https://itera-qa.azurewebsites.net/home/automation")
# driver.maximize_window()

#Select single checkbox
#driver.find_element(By.XPATH, "//input[@id='monday']").click()

#select multiple checkbox
# checkboxes = driver.find_elements(By.XPATH, "//*[@type='checkbox' and contains (@id,'day')]")
# print(len(checkboxes))

#Approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach1
# for checkbox in checkboxes:
#     checkbox.click()

# links = driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
# for link in links:
#     print(link.text, " ", link.id)

#alllinks = driver.find_elements(By.TAG_NAME,"a")
#count=0
# for link in alllinks:
#     url = link.get_attribute('href')
#     try:
#         res = requests.head(url)
#     except:
#         None
#     if res.status_code>=400:
#         print("broken link : ", url)
#         #count+=1
#     else:
#         print("Valid link : ", url)
# 
# time.sleep(10)
# driver.quit()

l=[1,2,3,4,5,2,3,4,7,9,5]
myset = set(l)

if l==myset:
    

