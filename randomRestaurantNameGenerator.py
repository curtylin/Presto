import random
from time import time, ctime
from datetime import datetime, date
from builtins import input
global currentHour, currentMinutes, currentDOW, inputFile

class Restaurant:
    name = ''
    category = ''
    distance = -1
    foodRating = -1
    cost = -1
    weekdayOpenTime = -1
    weekdayCloseTime = -1
    weekendOpenTime = -1
    weekendCloseTime = -1
    totalRating = -1

    def __init__(self, name, category, distance, foodRating, cost, wkdayOpen, wkdayClose, wkendOpen, wkendClose, totalRating):
        self.name = name
        self.category = category
        self.distance = distance
        self.foodRating = foodRating
        self.cost = cost
        self.weekdayOpenTime = wkdayOpen
        self.weekdayCloseTime = wkdayClose
        self.weekendOpenTime = wkendOpen
        self.weekendCloseTime = wkendClose
        self.totalRating = totalRating

def restaurantWillBeOpen(openTime, closeTime, restaurantDistanceRating):
    """ Returns True if the restaurant is currently open (based on the current time of the system)."""
    if openTime == 24 and closeTime == 24:
        return True
    minutesToDestination = (30-5*(restaurantDistanceRating - 1))/2
    currentTimeConverted = currentHour + currentMinutes/60
    timeAtDestination = currentTimeConverted + minutesToDestination/60
    writeLog.write('[' + str(datetime.now()) + '] Time At Arrival: ' + str(timeAtDestination)+ '\n')
    return timeAtDestination >= openTime and timeAtDestination < closeTime

def parseFoodRating(inputFoodRating):
    """" Returns the input as a float if it is a valid rating, else gives '6' as a rating to put more weight to the restaurant since it has not been visited before."""
    if inputFoodRating == '#DIV/0!' and userFeelsAdventurous:
        return float(99)
    elif inputFoodRating == '#DIV/0!':
        return float(6)
    else:
        return float(inputFoodRating)
    
def parseDistanceRating(inputDistanceRating):
    if userIsReallyHungry and float(inputDistanceRating) == 1:
        return 0
    elif userIsReallyHungry and float(inputDistanceRating) <= 3:
        return float(inputDistanceRating) + 1
    else:
        return float(inputDistanceRating)

def parseCostRating(inputCostRating):
    if userWantsCheapEat and float(inputCostRating) == 1:
        return 0
    elif userWantsCheapEat and float(inputCostRating) <= 3:
        return float(inputCostRating) + 1
    else:
        return float(inputCostRating)

def isWeekend():
    """" Returns True if it is the weekend. """
    if currentDOW == 'Fri' or currentDOW == 'Sat' or currentDOW == 'Sun':
        return True
    else:
        return False

possibleDestinations = {}
currentTime = ctime(time())
currentHour = float(currentTime.split()[3][0:2])
currentMinutes = float(currentTime.split()[3][3:5])
currentDOW = str(currentTime.split()[0])
print('Current Time: ' +currentTime)

writeLogFileName = 'randomRestaurantNameGeneratorLog' + str(date.today()) + '.log'
writeLog = open(writeLogFileName, 'w', encoding='cp1252')

currentlyWeekend = isWeekend()
writeLog.write('[' + str(datetime.now()) + '] Is weekend?: ' + str(currentlyWeekend)+ '\n')

userHungerinput = input("Are you currently really hungry? (y/n): ")
userIsReallyHungry = False
if userHungerinput == 'Yes' or userHungerinput == 'y'or userHungerinput == 'Y':
    userIsReallyHungry = True
writeLog.write('[' + str(datetime.now()) + '] userIsReallyHungry?:' + str(userIsReallyHungry)+ '\n')

userCheapinput = input("Do you currently want to spend less? (y/n): ")
userWantsCheapEat = False
if userCheapinput == 'Yes' or userCheapinput == 'y'or userCheapinput == 'Y':
    userWantsCheapEat = True
writeLog.write('[' + str(datetime.now()) + '] userWantsCheapEat?:' + str(userWantsCheapEat)+ '\n')

userAdventurousinput = input("Do you want to try something new? (y/n): ")
userFeelsAdventurous = False
if userAdventurousinput == 'Yes' or userAdventurousinput == 'y'or userAdventurousinput == 'Y':
    userFeelsAdventurous = True
writeLog.write('[' + str(datetime.now()) + '] userFeelsAdventurous?:' + str(userFeelsAdventurous)+ '\n')

inputFile = open('restaurantsList.txt', 'r', encoding='cp1252')
for line in inputFile:
    currentLine = line.split()
    restaurantName = currentLine[0]
    restaurantCategory = currentLine[1]
    restaurantDistanceRating = parseDistanceRating(currentLine[2])
    restaurantFoodRating = parseFoodRating(currentLine[3])
    restaurantCostRating = parseCostRating(currentLine[4])
    restaurantWeekdayOpenTime = float(currentLine[5])
    restaurantWeekdayCloseTime = float(currentLine[6])
    restaurantWeekendOpenTime = float(currentLine[7])
    restaurantWeekendCloseTime = float(currentLine[8])
    writeLog.write('[' + str(datetime.now()) + ']: Reading Line:' + str(len(possibleDestinations)) 
    + ' Parsing Restaurant:' + restaurantName + ' \t Restaurant Category:' + restaurantCategory 
    + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) 
    + '\t weekday operating hours: ' + str(restaurantWeekdayOpenTime) + '/' + str(restaurantWeekdayCloseTime) 
    + '\t weekend operating hours: ' + str(restaurantWeekendOpenTime) + '/' + str(restaurantWeekendCloseTime) + '\n')

    if restaurantName in possibleDestinations:
        writeLog.write('[' + str(datetime.now()) + ']: Found Duplicate Restaurant Name entry in file. Are you sure this is correct?')
        continue

    if currentlyWeekend:
        writeLog.write('[' + str(datetime.now()) + ']: Is weekend?: ' + str(currentlyWeekend) + '\t Using Weekend Open Time.\n')
        restaurantOpenTime = restaurantWeekendOpenTime
        restaurantCloseTime = restaurantWeekendCloseTime
    else:
        writeLog.write('[' + str(datetime.now()) + ']: Is weekend?: ' + str(currentlyWeekend) + '\t Using Weekday Open Time.\n')
        restaurantOpenTime = restaurantWeekdayOpenTime
        restaurantCloseTime = restaurantWeekdayCloseTime

    if (userWantsCheapEat and restaurantCostRating == 0) or (restaurantDistanceRating == 0 and userIsReallyHungry):
        continue

    if restaurantWillBeOpen(restaurantOpenTime, restaurantCloseTime, restaurantDistanceRating):
        if userFeelsAdventurous:
            if restaurantFoodRating == 99:
                writeLog.write('[' + str(datetime.now()) + ']: Added Currently Open Restaurant:' + restaurantName + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) + '\toperating hours: ' + str(restaurantOpenTime) + '/' + str(restaurantCloseTime) + '\n')
                totalRating = (((restaurantDistanceRating) + restaurantFoodRating + restaurantCostRating)*1000)
                possibleDestinations[restaurantName] = Restaurant(restaurantName, restaurantCategory, restaurantDistanceRating, restaurantFoodRating, restaurantCostRating, restaurantWeekdayOpenTime, restaurantWeekdayCloseTime, restaurantWeekendOpenTime, restaurantWeekendCloseTime, totalRating)
                continue
            continue
        writeLog.write('[' + str(datetime.now()) + ']: Added Currently Open Restaurant:' + restaurantName + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) + '\toperating hours: ' + str(restaurantOpenTime) + '/' + str(restaurantCloseTime) + '\n')
        totalRating = (((restaurantDistanceRating) + restaurantFoodRating + restaurantCostRating)*1000)
        possibleDestinations[restaurantName] = Restaurant(restaurantName, restaurantCategory, restaurantDistanceRating, restaurantFoodRating, restaurantCostRating, restaurantWeekdayOpenTime, restaurantWeekdayCloseTime, restaurantWeekendOpenTime, restaurantWeekendCloseTime, totalRating)

writeLog.write('[' + str(datetime.now()) + '] Finished parsing and adding unique restaurants. Now starting the process of returning random restaurant choice.\n')

possibleEntries = []
for restaurant in possibleDestinations:
    writeLog.write('[' + str(datetime.now()) + '] Giving ' + str(possibleDestinations[restaurant].totalRating) + ' entries to ' + restaurant + '\n')
    for i in range(int(possibleDestinations[restaurant].totalRating)):
        possibleEntries.append(restaurant)

writeLog.write('[' + str(datetime.now()) + '] Finished adding restaurant entries.\n')

if len(possibleEntries) == 0:
    writeLog.write('[' + str(datetime.now()) + '] List of possibleEntries is empty! \n')
    print("There is currently nothing open! If this is incorrect, check log for more details.")
else:
    winningEntry = random.randrange(len(possibleEntries))
    writeLog.write('[' + str(datetime.now()) + '] Winning entry: ' + str(winningEntry) + '...\t possibleEntries[' + str(winningEntry) + '] = ' + str(possibleEntries[winningEntry]) + '\n')
    print('The result is: ' + possibleEntries[winningEntry] + '. They close at: ' + str(possibleDestinations[possibleEntries[winningEntry]].weekendCloseTime))


inputFile.close()
writeLog.write('[' + str(datetime.now()) + '] Closing inputFile and writeLog. Expected EOM.\n')
userCheapinput = input("--End of Program. Press any key to close the window.--")
writeLog.close()