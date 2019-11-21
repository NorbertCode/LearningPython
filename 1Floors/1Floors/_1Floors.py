
def checkIfNumber():
    tempInput = input()
    if tempInput.isdigit():
        return float(tempInput)
    elif tempInput.count(".") > 0 and tempInput.count(".") < 2:
        return float(tempInput)
    else:
        print("The entered value is not a number. Please try again.")
        checkIfNumber()

def shortenIfPossible(floatToShorten):
    newString = str(floatToShorten)
    while newString.endswith("0") or newString.endswith("."):
        newString = newString[:-1]

    return newString
    

print("Width of floor: ", end="")
width = checkIfNumber()
print("Height of floor: ", end="")
height = checkIfNumber()
print("Cost of floor per m^2: ", end="")
cost = checkIfNumber()

totalArea = width * height
totalCost = totalArea * cost
print("The floor is " + shortenIfPossible(totalArea) + "m^2 and it costs " + shortenIfPossible(totalCost) + " of your currency.")