import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from lxml import etree


URL="https://www.conted.ox.ac.uk/profiles#?subject=&format="



webpage=requests.get(URL)
soup=BeautifulSoup(webpage.content,'html.parser')
dom=etree.HTML(str(soup))
#<div class="campl-side-padding"><div class="field field-name-title field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even" property="dc:title"><h3><a href="/directory/professor-gabor-betegh">Professor  Gábor Betegh</a></h3></div></div></div><div class="field field-name-field-sd-job-titles field-type-text field-label-hidden"><div class="field-items"><div class="field-item even">Laurence Professor of Ancient Philosophy</div></div></div><div class="field field-name-field-sd-office-phone field-type-text field-label-hidden"><div class="field-items"><div class="field-item even">01223 767500</div></div></div><div class="field field-name-field-sd-email-address field-type-email field-label-hidden"><div class="field-items"
d=soup.find_all('div' ,'col-xs-6 col-sm-4 col-md-3 col-lg-2 profile')
#d=soup.find_all('a' )

l1=[]
for i in d:
    if i != None:

        l1.append(i.text)

org = map(lambda s: s.strip(), l1)



l2=list(org)


l3=[]
for i in l2:
    va =i.split("\n")
    for j in va:
        l3.append(j)

# print(l3)
d4=[]
d5 =[]
for l in range(len(l3)):
    if l%2==0:
        d4.append(l3[l])
    else:
        d5.append(l3[l])


# df ={"Academic staff Name":d4,"Designation":d5}
# dataset=pd.DataFrame(data=df)
# dataset.to_csv('Oxford_University.csv')

# s=soup.find_all('a','href')
# print(s)
productLinks = soup.findAll('a', attrs={'class' : 'col-xs-6 col-sm-4 col-md-3 col-lg-2 profile'})
for link in productLinks:
    print (link['href'])
