"
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
    

"
class Vendors:
    def __init__(self, line, name, typeOfFood):
        self.line = int(line)
        self.name = name
        self.typeOfFood = typeOfFood
        self.time = 0


