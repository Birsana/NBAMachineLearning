#Unfortuntaly, the HTML on the espn and NBA player stats page is a mess, so I found it too time consuming to scrape
#the data directly from the site. Since all the data fit on one page (unlike the 10+ pages for the salaries section),
#I decided to just copy and paste the table into a text file and use that.

#URL: https://stats.nba.com/leaders/?Season=2018-19&SeasonType=Regular%20Season

import re
import pandas as pd
players = []

#the following arrays represent stats that NBA.com tracks. Honestly, as a casual basketball fan I don't know what
#some of them even mean.

GP = []
MIN = []
PTS = []
FGM = []
FGA = []
FGPERCENT = []
THREEPM = []
THREEPA = []
THREEPERCENT = []
FTM = []
FTA = []
FTPERCENT = []
OREB = []
DREB = []
REB = []
AST = []
STL = []
BLK = []
TOV = []
EFF = []


data = open("./nbastats1819.txt", "r") #change to get previous year's data



raw = data.readlines()
for i in range(len(raw)):
    raw[i] = raw[i].rstrip()

for i in range(len(raw)):
    if re.search('[a-zA-Z]', raw[i]):
#this was very tedious and there was probably a faster way of doing it
        players.append(raw[i])
        GP.append(raw[i+1])
        MIN.append(raw[i + 2])
        PTS.append(raw[i + 3])
        FGM.append(raw[i + 4])
        FGA.append(raw[i + 5])
        FGPERCENT.append(raw[i + 6])
        THREEPM.append(raw[i + 7])
        THREEPA.append(raw[i + 8])
        THREEPERCENT.append(raw[i + 9])
        FTM.append(raw[i + 10])
        FTA.append(raw[i + 11])
        FTPERCENT.append(raw[i + 12])
        OREB.append(raw[i + 13])
        DREB.append(raw[i + 14])
        REB.append(raw[i + 15])
        AST.append(raw[i + 16])
        STL.append(raw[i + 17])
        BLK.append(raw[i + 18])
        TOV.append(raw[i + 19])
        EFF.append(raw[i + 20])


df = pd.DataFrame(
    {
        'Players': players,
        'GP': GP,
        'MIN': MIN,
        'PTS': PTS,
        'FGM': FGM,
        'FGA': FGA,
        'FG%': FGPERCENT,
        '3PM': THREEPM,
        '3PA': THREEPA,
        '3P%': THREEPERCENT,
        'FTM': FTM,
        'FTA': FTA,
        'FT%': FTPERCENT,
        'OREB': OREB,
        'DREB': DREB,
        'REB': REB,
        'AST': AST,
        'STL': STL,
        'BLK': BLK,
        'TOV': TOV,
        'EFF': EFF,
    })


df.to_csv('2019stats.csv') #change to get previous year's data