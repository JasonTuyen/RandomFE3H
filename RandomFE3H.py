"""
create a GUI
no DLC characters yet
"""

import csv
import random
import tkinter

mainChar = ["Bylad", "Bylass"]
lordChar = ["Cyril", "Edelgard", "Dimitri", "Claude"]
route = []

def routePath(value):
        switcher={
            "Church"      : "church_route.csv",
            "Black Eagles": "be_route.csv",
            "Blue Lions"  : "bl_route.csv",
            "Golden Deer" : "gd_route.csv",
        }
        return switcher.get(value,"Invalid route, try again")

value = input("Are you playing as 'Bylad' (Male Byleth) or 'Bylass' (Female Byleth)? Type either 'Bylad' or 'Bylass'.\n")
while value != "Bylad" or "Bylass":
    if value == "Bylad":
        main = 0
        mainCharGender = "M"
        break
    elif value == "Bylass":
        main = 1
        mainCharGender = "F"
        break
    else:
        value = input("Are you playing as 'Bylad' (Male Byleth) or 'Bylass' (Female Byleth)? Type either 'Bylad' or 'Bylass'.\n")
print(f'You are playing as {value}.\n')
    
value = input("Which route are you playing: 'Church', 'Black Eagles', 'Blue Lions', 'Golden Deer'?\n")
while value != "Church" or "Black Eagles" or "Blue Lions" or "Golden Deer":
    if routePath(value) == "church_route.csv":
        lord = 0
        lordCharGender = "M"
        break
    elif routePath(value) == "be_route.csv":
        lord = 1
        lordCharGender = "F"
        break
    elif routePath(value) == "bl_route.csv":
        lord = 2
        lordCharGender = "M"
        break
    elif routePath(value) == "gd_route.csv":
        lord = 3
        lordCharGender = "M"
        break
    else:
        value = input("Which route are you playing: 'Church', 'Black Eagles', 'Blue Lions', 'Golden Deer'?\n")
print(f'You are playing the {value} route.\n')

file = open("FE3H_classes.csv", 'r')
reader = csv.reader(file)
chosenClass = random.choice(list(reader))
file.close()
if str(chosenClass[5]) == "" and (mainCharGender == chosenClass[4] or chosenClass[4] == ""): 
            print(mainChar[main],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]))
else:
    while str(chosenClass[5]) != "" or (mainCharGender != chosenClass[4] and chosenClass[4] != ""):
        file = open("FE3H_classes.csv", 'r')
        reader = csv.reader(file)
        chosenClass = random.choice(list(reader))
        file.close()
    print(mainChar[main],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]))

file = open("FE3H_classes.csv", 'r')
reader = csv.reader(file)
chosenClass = random.choice(list(reader))
file.close()
if (str(chosenClass[5]) == str(lordChar[lord]) or str(chosenClass[5]) == "") and (lordCharGender == chosenClass[4] or chosenClass[4] == ""): 
        print(lordChar[lord],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]),(chosenClass[5]))
else:
    while (str(chosenClass[5]) != str(lordChar[lord]) and str(chosenClass[5]) != "") or (lordCharGender != chosenClass[4] and chosenClass[4] != ""):
        file = open("FE3H_classes.csv", 'r')
        reader = csv.reader(file)
        chosenClass = random.choice(list(reader))
        file.close()
    print(lordChar[lord],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]),(chosenClass[5]))

while len(route) < 10:

    file = open(routePath(value), 'r')
    reader = csv.reader(file)
    chosenChar = random.choice(list(reader))
    file.close()

    file = open("FE3H_classes.csv", 'r')
    reader = csv.reader(file)
    chosenClass = random.choice(list(reader))
    file.close()

    if chosenChar[0] not in route:

        if len(route) == 9:
            print(chosenChar[0] + " Dancer")
            break

        if str(chosenClass[5]) == "" and (chosenChar[1] == chosenClass[4] or chosenClass[4] == ""): 
            print(chosenChar[0],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]))

        else:

            while (chosenClass[5]) != "" or (chosenChar[1] != chosenClass[4] and chosenClass[4] != ""):
                file = open("FE3H_classes.csv", 'r')
                reader = csv.reader(file)
                chosenClass = random.choice(list(reader))
                file.close()
            print(chosenChar[0],(chosenClass[0]),(chosenClass[1]),(chosenClass[2]),(chosenClass[3]))
        
        route.append(chosenChar[0])
