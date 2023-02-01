from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

fn=[]
position=[]
org=[]
email=[]
pages=list(range(1,118,10))
for page in pages:
    req = requests.get(f"https://search.ucl.ac.uk/s/search.html?query=careers&collection=website-meta&profile=_directory&tab=directory&start_rank={page}").text
    # print(req.text)
    soup = BeautifulSoup(req,'html.parser')
    # print(soup.prettify())
    profile = soup.find_all('ul',class_='profile-details')
    # print(profile)
    # print(page)
    # print(len(profile))
    for i in profile:
        fn.append(i.find('li',class_="fn").text)
        position.append(i.find('li',class_="position").text)
        org.append(i.find('li',class_="org").text)
        email.append(i.find('li',class_="email").text)

fn = map(lambda s: s.strip(), fn)
# print(list(fn))
fn1=list(fn)
position = map(lambda s: s.strip(), position)
# print(list(position))
position1=list(position)
org = map(lambda s: s.strip(), org)
# print(list(org))
org1=list(org)
email = map(lambda s: s.strip(), email)
# print(list(email))
email1=list(email)
df = {'Name':fn1,'Position':position1,"Organisation":org1,"Email":email1}

dataset = pd.DataFrame(data=df)
# print(dataset)
dataset.to_csv('univercity.csv')
