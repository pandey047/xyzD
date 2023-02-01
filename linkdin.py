from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome(executable_path=r"C:\Users\umeshpandey\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com')
# time.sleep(5)

signInButton=driver.find_element("xpath",'/html/body/nav/div/a[2]')

signInButton.click()

email=driver.find_element('xpath','//*[@id="username"]')
email.send_keys('pandey047@gmail.com')

password=driver.find_element('xpath','//*[@id="password"]')
password.send_keys('admin@102')

loginBtn=driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button')
loginBtn.click()
# time.sleep(4)
driver.get('https://www.linkedin.com/school/oxforduni/')
# driver.quit()
# empBtn=driver.find_element()
# div = driver.find_element('class','display-flex mt2 mb1')


driver.find_element('xpath','//*[@id="ember30"]').click()
print("Inside staff list")

staff=driver.find_elements('xpath','//*[@id="thetrQvxQR2zk2UfSAIhcw=="]/div/ul')
print('----',staff)
#var=driver.find_elements('xpath','//*[@id="thetrQvxQR2zk2UfSAIhcw=="]/div/ul/li[1]/div/div/div[2]')
# var=driver.find_elements('class','entity-result')
# var=driver.find_elements(By.TAG_NAME, 'ul')
# wait = WebDriverWait(driver, 5)
# var=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="thetrQvxQR2zk2UfSAIhcw=="]/div/ul')))
# print('---',var)
# for i in var:
#     print(i.text)
# for i in var:
#     print(i.text)
# res=requests.get('https://www.linkedin.com/search/results/people/?currentCompany=%5B%224477%22%2C%2218749425%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&sid=S~O').text
# # src = driver.page_source
# soup=BeautifulSoup(res,'html.parser')
# print(soup.text)
# staff=soup.find('div',attrs={'class':'reusable-search__entity-result-list list-style-none'})
# print(staff)

# div.find_element_by_css_selector('a').get_attribute('href')
#//*[@id="ember29"]/span #//*[@id="ember234"]/span
# print(div) #//*[@id="ember800"]
# div.click()
time.sleep(5)