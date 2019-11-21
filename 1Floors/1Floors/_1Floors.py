
def checkIfNumber():
    tempInput = input()
    if tempInput.isdigit():
        return float(tempInput) #If the string is a number convert it to float and return it.
    elif tempInput.count(".") > 0 and tempInput.count(".") < 2:
        return float(tempInput) #If it's a floating point number convert it and return it.
    else:
        print("The entered value is not a number. Please try again.")
        checkIfNumber() #If it's not a number try again.

def shortenIfPossible(floatToShorten):
    newString = str(floatToShorten)
    while newString.endswith("0") or newString.endswith("."):
        newString = newString[:-1] #Shorten it if it ends with 0 or .

    return newString
    
#Get input from the user
print("Width of floor: ", end="")
width = checkIfNumber()
print("Height of floor: ", end="")
height = checkIfNumber()
print("Cost of floor per m^2: ", end="")
cost = checkIfNumber()

#Calculate everything
totalArea = width * height
totalCost = totalArea * cost
#Print the answer
print("The floor is " + shortenIfPossible(totalArea) + "m^2 and it costs " + shortenIfPossible(totalCost) + " of your currency.")
