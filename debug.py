import requests
from bs4 import BeautifulSoup
import json
import csv
res = requests.get('https://register-api.officeforstudents.org.uk/api/Provider/Name').text
print(res,type(res))



to_csv = json.loads(res)
from operator import itemgetter
newlist = sorted(to_csv, key=itemgetter('Name'))

print(newlist,type(newlist),len(newlist))
keys = newlist[0].keys()

with open('people.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(newlist)
