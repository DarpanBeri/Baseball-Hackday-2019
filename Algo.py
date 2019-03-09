import csv
"""
    Algorithm that chooses where the user to go to get his food.

    Input: Quadrant and Food Option seleted

    Additonal stuff from .csv s: Historical data telling how much time per person to get food(in an unique inning), Realtime data telling number of people in a line, Vendors info telling about food available
    Stuff hardcoded: Current Inning, ment to be recieved from an API, which cant be used rn

    Output: A string which says "Based of your food prefrences, " + x + y + z " are your best options as they have a waiting time of " + a +b +c

    1. Parse the input, to FoodPref = y
    2. Datastructres setup:
        a. Set of Burger vendors with current number of people
        b. Multiply all of them with Historical data for burgers
        c. Find the least 3 values and their key.

    3. Output:
        the stuff discussed above


    1) Based on food type find the shortestLine
    2) Based on food type fin the closestLine
    3) if (closestLine-shortestLine)<3 go to closestLine else go to shortestLine


"""
"""arline=[2,3,4,6,7,8,9.12]
arname = ["hotdog1","hotdog2","hotdog3","hotdog4","burger1","burger2","burger3","burger4"]
arTypeOfFood = [1,1,1,1,2,2,2,2]"""

class Vendor:
    def __init__(self, line, name, typeOfFood, perperson):
        self.line = int(line)
        self.name = name
        self.typeOfFood = typeOfFood
        self.time = 0
        self.perperson = int(perperson)


# Take in .csv file and make Arrays
artypeOfFood = [] # array for type of food
arname = []
with open('CSVs/vendors.csv', newline='') as csvfile:
    vendors = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in vendors:
        artypeOfFood.append(row[1])
        arname.append(row[0])

arline = [] # array for current line at vendor
with open('CSVs/realtimedata_-_Sheet1-2.csv', newline='') as csvfile:
    currline = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in currline:
        arline.append(row[1])

artime = [] # array for time per person based on the inning
with open('CSVs/historical_Data_-_Sheet1.csv', newline='') as csvfile:
    time = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in time:
        artime.append(row[1])

artypeOfFood.remove('type of food')
arname.remove("vendor's name")
artime.remove("1H")




arVendors = []
for i in range(8):
    arVendors.append(Vendor(arline[i], arname[i], artypeOfFood[i], artime[i]))

for i in range(8):
    arVendors[i].time = arVendors[i].line * arVendors[i].perperson


    



