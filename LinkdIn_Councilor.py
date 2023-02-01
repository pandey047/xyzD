import requests,time,random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

'''
# browser.get('https://www.linkedin.com/uas/login')
# file=open('config.txt')

# lines=file.readlines()
# username=lines[0]
# password=lines[1]

# elementID=browser.find_element(By.ID,'username')
# # print(elementID)
# elementID.send_keys(username)
# elementID=browser.find_element(By.ID,'password')
# # print(elementID)
# elementID.send_keys(password)

# elementID.submit()

'''
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
# print(elementID)
elementID.send_keys(username)
elementID=driver.find_element(By.ID,'password')
# print(elementID)
elementID.send_keys(password)

elementID.submit()

# driver.find_element(By.CSS_SELECTOR,'#session_key').send_keys(email)
# driver.find_element(By.CSS_SELECTOR,'#session_password').send_keys(password)
# driver.find_element(By.CSS_SELECTOR,"body > main > section.section.section--hero > div.sign-in-form-container > form > button").click()
# driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button').click()

# WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "global-nav")))
print("Login Successful.")
emp_name=[]
roll=[]
pages=range(1,29)
for page in pages:
    link=f'https://www.linkedin.com/search/results/people/?currentCompany=%5B%22128441%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page={page}&sid=%40Ek'
    driver.get(link)
    src=driver.page_source
    # print(src)

    soup=BeautifulSoup(src,'lxml')
    # print(soup)
    st=soup.find_all('li',attrs={'class':'reusable-search__result-container'})
    # print(st)
    # sname=st.find('li',attrs={'class':'reusable-search__result-container'})

    for i in st:
        nm=i.find('span',attrs={'aria-hidden':'true'})
        if nm:
            emp_name.append(i.find('span',attrs={'aria-hidden':'true'}).text)
        else:
            emp_name.append('LinkedIn Member')
        de=i.find('div',attrs={'entity-result__primary-subtitle t-14 t-black t-normal'})
        if de:
            roll.append(de.text.strip())
        else:
            roll.append('---')

# roll1=roll.strip()
# t = map(lambda s: s.strip(), r)

df = {'Name':emp_name,'Position':roll}

dataset = pd.DataFrame(data=df)

print(dataset)
# print(dataset)
dataset.to_csv('East Kent College.csv')
print(len(roll))
print(len(emp_name))

