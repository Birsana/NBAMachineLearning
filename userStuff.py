from MLCode import optimalTheta
import re
import pandas as pd
import numpy as np

df = pd.read_csv('2019stats.csv')
statsTrackedStr = "GP MIN PTS FGM FGA FG% 3PM 3PA 3P% FTM FTA FT% OREB DREB REB AST STL BLK TOV EFF"
statsTracked = statsTrackedStr.split()

saved_column = df.Players

players = []

for i in saved_column:
    players.append(i)

players = [player.lower() for player in players]
def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def statsPicker(num):
    for i in range(num):
        stat = statsTracked[i]
        print("Enter a value for %s, or just press enter to have it automatically filled in" % stat)
        statUser = input().strip()
        if statUser == "":
            statUser = float(df["%s" % stat].mean())
            userData.append(statUser)
            continue
        while isFloat(statUser) == False:
            print("Please enter a number")
            statUser = input().strip()
        while float(statUser) < 0 or float(statUser)> 100000:
            print("Please enter a number between 0 and 100000")
            statUser = input().strip()
        userData.append(statUser)
    return

userData = [1]

userChoice = input("Enter 1 to choose a player, or 2 to choose specific stats").strip()

while userChoice != "1" and userChoice != "2":
    userChoice = input("Please enter either 1 or 2").strip()

if userChoice == "2":
    print("These are the following stats you can enter. If you leave a certain stat blank, the algorithm"
          " will fill it in with the average from the training data set.")
    print("GP MIN PTS FGM FGA FG% 3PM 3PA 3P% FTM FTA FT% OREB DREB REB AST STL BLK TOV EFF")
    print("This program can be messed around with theoretically impossible values, like averaging 100 points"
          " a game, as well as mathematically impossible values, like a 120% 3 point accuracy. \nAs long as the"
          " value you input is positive and less than 100000 (let's not get too crazy here), it will work.")
    statsPicker(len(statsTracked))
    userDataM = np.asarray(userData)
    userDataM = userDataM.astype(float)
    salary = (userDataM@optimalTheta)[0]
    print(int(round(salary)))




playerIndex = 0
if userChoice == "1":
    print("When you enter an NBA player, our program checks NBA.com for the following stats:")
    print("GP MIN PTS FGM FGA FG% 3PM 3PA 3P% FTM FTA FT% OREB DREB REB AST STL BLK TOV EFF")
    print("At the url https://stats.nba.com/leaders/ for the 18/19 season. "
          "This page includes any player who played at least 70% of their team's games last season.")
    print("Please enter a player")

    player = input().lower().strip()
    while player not in players:
        print("Uh oh! It looks like the player you've entered isn't displayed on that page. Please enter"
              " a valid player")
        player = input().lower().strip()
    playerIndex = players.index(player)
    index = [0,1]
    playerData = np.array(df.loc[playerIndex,:])

    playerData = np.delete(playerData, index)
    playerData = playerData[np.newaxis, :]
    playerData = np.insert(playerData, 0, 1)
    playerData = playerData.astype(float)
    salary = (playerData@optimalTheta)[0]

    print(int(round(salary)))


    print("In training my program was usually off by an average of 4 million dollars. If it is off by a siginificant"
          " amount with a certain player, \nthat could suggest this players is either very overpaid/underpaid,"
          "or had an execeptionally good/bad season. I've found that it is most accurate in prediciting\n"
          "the salary of average players, and unpredicts top players, while overpredicting weaker players.")


