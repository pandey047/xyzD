from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


result = requests.get("https://www.educ.cam.ac.uk/contact/staffcontact.html")
soup=BeautifulSoup(result.text,'html.parser')
# print(soup)

staff=soup.find('div',class_='stafflist')
fn=[]
ph=[]
em=[]
build=[]
for i in soup.find_all('div',attrs={'class':'personrow'}):
    name = i.find('div', attrs={'class': 'name'})
    fn.append(name.text)
    phone=i.find('div', attrs={'class': 'phone'})
    ph.append(phone.text)
    email=i.find('div', attrs={'class': 'email'})
    em.append(email.text)
    building=i.find('div', attrs={'class': 'building'})
    build.append(building.text)



df = {'Faculty Name':fn,'Email':em,"Contact Number":ph,"Building":build}
dataset = pd.DataFrame(data=df)
dataset.to_csv('cambridge_data.csv')


