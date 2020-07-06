import random
from time import time, ctime
from datetime import datetime, date
global currentHour, currentDOW, inputFile

possibleDestinations = {}
currentTime = ctime(time())
currentHour = float(currentTime.split()[3][0:2])
currentDOW = str(currentTime.split()[0])
print(currentTime)

writeLogFileName = 'randomRestaurantNameGeneratorLog' + str(date.today()) + '.log'
writeLog = open(writeLogFileName, 'w', encoding='cp1252')


def restaurantIsOpen(openTime, closeTime):
    """ Returns True if the restaurant is currently open (based on the current time of the system)."""
    if openTime == 24 and closeTime == 24:
        return True
    return currentHour >= openTime and currentHour < closeTime

def checkValidRating(input):
    """" Returns the input as a float if it is a valid rating, else gives '6' as a rating to put more weight to the restaurant."""
    if input == '#DIV/0!':
        return float(6)
    else:
        return float(input)

def isWeekend():
    """" Returns True if it is the weekend. """
    if currentDOW == 'Fri' or currentDOW == 'Sat' or currentDOW == 'Sun':
        return True
    else:
        return False

currentlyWeekend = isWeekend()
writeLog.write('[' + str(datetime.now()) + '] Is weekend?: ' + str(currentlyWeekend))

inputFile = open('restaurantsList.txt', 'r', encoding='cp1252')
for line in inputFile:
    input = line.split()
    restaurantName = input[0]
    restaurantCategory = input[1]
    restaurantDistanceRating = checkValidRating(input[2])
    restaurantFoodRating = checkValidRating(input[3])
    restaurantCostRating = checkValidRating(input[4])
    restaurantWeekdayOpenTime = float(input[5])
    restaurantWeekdayCloseTime = float(input[6])
    restaurantWeekendOpenTime = float(input[7])
    restaurantWeekendCloseTime = float(input[8])
    writeLog.write('[' + str(datetime.now()) + ']: Reading Line:' + str(len(possibleDestinations.keys)) 
    + ' Parsing Restaurant:' + restaurantName + ' \t Restaurant Category:' + restaurantCategory 
    + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) 
    + '\t weekday operating hours: ' + str(restaurantWeekdayOpenTime) + '/' + str(restaurantWeekdayCloseTime) 
    + '\t weekend operating hours: ' + str(restaurantWeekendOpenTime) + '/' + str(restaurantWeekendCloseTime) + '\n')

    if restaurantName in possibleDestinations:
        writeLog.write('[' + str(datetime.now()) + ']: Found Duplicate Restaurant Name entry in file. Are you sure this is correct?')
        continue
    if currentlyWeekend:
        writeLog.write('[' + str(datetime.now()) + '] Is weekend?: ' + str(currentlyWeekend) + '\t Using Weekend Open Time.\n')
        restaurantOpenTime = restaurantWeekendOpenTime
        restaurantCloseTime = restaurantWeekendCloseTime
    else:
        writeLog.write('[' + str(datetime.now()) + '] Is weekend?: ' + str(currentlyWeekend) + '\t Using Weekday Open Time.\n')
        restaurantOpenTime = restaurantWeekdayOpenTime
        restaurantCloseTime = restaurantWeekdayCloseTime

    if restaurantIsOpen(restaurantOpenTime, restaurantCloseTime):
        writeLog.write('[' + str(datetime.now()) + ']: Added Currently Open Restaurant:' + restaurantName + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) + '\toperating hours: ' + str(restaurantOpenTime) + '/' + str(restaurantCloseTime) + '\n')
        possibleDestinations[restaurantName] = (((restaurantDistanceRating+1) + restaurantFoodRating + restaurantCostRating)*1000)

writeLog.write('[' + str(datetime.now()) + '] Finished parsing and adding unique restaurants. Now starting the process of returning random restaurant choice.\n')

possibleEntries = []
for restaurant in possibleDestinations:
    writeLog.write('[' + str(datetime.now()) + '] Giving ' + str(possibleDestinations[restaurant]) + ' entries to ' + restaurant + '\n')
    for i in range(int(possibleDestinations[restaurant])):
        possibleEntries.append(restaurant)

writeLog.write('[' + str(datetime.now()) + '] Finished adding restaurant entries.\n')

if len(possibleEntries) == 0:
    writeLog.write('[' + str(datetime.now()) + '] List of possibleEntries is empty! \n')
    print("There is currently nothing open! If this is incorrect, check log for more details.")
else:
    winningEntry = random.randrange(len(possibleEntries))
    writeLog.write('[' + str(datetime.now()) + '] Winning entry: ' + str(winningEntry) + '...\t possibleEntries[' + str(winningEntry) + '] = ' + str(possibleEntries[winningEntry]) + '\n')
    print(possibleEntries[winningEntry])

inputFile.close()
writeLog.write('[' + str(datetime.now()) + '] Closing inputFile and writeLog. Expected EOM.\n')
writeLog.close()