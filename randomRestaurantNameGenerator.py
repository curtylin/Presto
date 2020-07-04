import random
from time import time, ctime
from datetime import datetime, date
global currentHour, currentDOW, inputFile, currentLine

possibleDestinations = {}
currentTime = ctime(time())
currentHour = float(currentTime.split()[3][0:2])
currentDOW = str(currentTime.split()[0])
currentLine = 0

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

if isWeekend():
    inputFile = open('foodList-Weekend.txt', 'r', encoding='cp1252')
    writeLog.write('[' + str(datetime.now()) + '] Is weekend?: ' + str(isWeekend()) + '\t Reading inputs from: foodList-Weekend.txt\n')
else:
    inputFile = open('foodList-Weekday.txt', 'r', encoding='cp1252')
    writeLog.write('[' + str(datetime.now()) + '] Is Weekend: ' + str(isWeekend()) + '\t Reading inputs from: foodList-Weekday.txt\n')

for line in inputFile:
    input = line.split()
    restaurantName = input[0]
    restaurantDistanceRating = checkValidNumber(input[1])
    restaurantFoodRating = checkValidNumber(input[2])
    restaurantCostRating = checkValidNumber(input[3])
    restaurantOpenTime = float(input[4])
    restaurantCloseTime = float(input[5])
    writeLog.write('[' + str(datetime.now()) + ']: Reading Line:' + str(currentLine) + ' Parsing Restaurant:' + restaurantName + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) + '\toperating hours: ' + str(restaurantOpenTime) + '/' + str(restaurantCloseTime) + '\n')

    if restaurantName in possibleDestinations:
        continue
    elif restaurantIsOpen(restaurantOpenTime, restaurantCloseTime):
        writeLog.write('[' + str(datetime.now()) + ']: Added Currently Open Restaurant:' + restaurantName + '\tdistance rating: ' + str(restaurantDistanceRating) + '\tfood rating: ' + str(restaurantFoodRating) + '\tcost rating: ' + str(restaurantCostRating) + '\toperating hours: ' + str(restaurantOpenTime) + '/' + str(restaurantCloseTime) + '\n')
        possibleDestinations[restaurantName] = ((restaurantDistanceRating + restaurantFoodRating + restaurantCostRating)*1000)
    currentLine+=1

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