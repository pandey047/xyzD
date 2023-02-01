import requests,time,random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
email = ""
password = ""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
# driver.get("https://www.linkedin.com/") 
driver.get('https://www.linkedin.com/uas/login') 
# WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"#session_key")))
file=open('config.txt')

lines=file.readlines()
username=lines[0]
password=lines[1]

elementID=driver.find_element(By.ID,'username')

elementID.send_keys(username)
elementID=driver.find_element(By.ID,'password')

elementID.send_keys(password)

elementID.submit()

print("Login Successful.")
# emp_name=[]
# roll=[]
# pages=range(1,5)
# driver.find_element(By.CLASS_NAME,'app-aware-link  global-nav__primary-link').click()
# driver.implicitly_wait(10)

link='https://www.linkedin.com/sales/search/people?_ntb=%2FDSN1EaFSpe0kFaeVMNAlA%3D%3D&query=(recentSearchParam%3A(id%3A2152055922%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A11913585%2Ctext%3AAshfield%2520District%2520Council%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A6%2Ctext%3ADirector%2CselectionType%3AINCLUDED)%2C(id%3A7%2Ctext%3AVP%2CselectionType%3AINCLUDED)%2C(id%3A8%2Ctext%3ACXO%2CselectionType%3AINCLUDED)))))&sessionId=3XUm3hAOSomv2LSKdBKFSw%3D%3D'
res=requests.get(link)
# driver.get(link)
# driver.implicitly_wait(10)
#name= driver.find_elements(By.TAG_NAME,'ol'):

# src=driver.page_source
# soup=BeautifulSoup(src,'lxml')
soup=BeautifulSoup(res.text,'lxml')
st=soup.find_all('div',attrs={'class':'artdeco-entity-lockup__subtitle ember-view t-14'})
print(st)
# driver.implicitly_wait(5)
# name=soup.find('div',attrs={'class':'artdeco-entity-lockup__subtitle ember-view t-14'})
# print(name)
