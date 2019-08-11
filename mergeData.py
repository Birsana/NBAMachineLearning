import csv
#Type the following command in the terminal window once you have all of your csv files:
#cat 2015FinalData.csv 2016FinalData.csv 2017FinalData.csv 2018FinalData.csv 2019FinalData.csv > NBA.csv


with open('2019Salary.csv') as f: #change based on which files you want to merge
    reader = csv.reader(f)
    dataList = list(reader)

with open('2019stats.csv') as g: #change based on which files you want to merge
    reader = csv.reader(g)
    dataList2 = list(reader)


for i in dataList:
    for j in dataList2:
        if i[1] in j:
            j.append(i[2])


with open("2019FinalData.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dataList2)

