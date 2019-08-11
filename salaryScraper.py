import pandas as pd
import requests
from bs4 import BeautifulSoup


playersFinal = []
salariesFinal = []

getTextArray = []

for i in range(1, 16): #change number of loops based on how many pages it has
    url = 'http://www.espn.com/nba/salaries/_/year/2015/page/%s/seasontype/4' %(i) #change url based on what year you want

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_= 'tablehead')
    salaries = table.find_all('td')
    if len(salaries) == 0:
        break
    for salary in salaries:
        text=salary.get_text()
        getTextArray.append(text)

index = 1
sep = ','
for i in range(len(getTextArray)):
    if getTextArray[i] == str(index):
        playersFinal.append(getTextArray[i+1].split(sep,1)[0])
        salariesFinal.append(getTextArray[i+3])
        index += 1

df = pd.DataFrame(
    {
        'Players': playersFinal,
        'Salaries': salariesFinal
    })

df.to_csv('2015Salary.csv') #change based on what year you want




