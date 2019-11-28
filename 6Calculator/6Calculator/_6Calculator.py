from math import sqrt
from time import sleep

#Function for checking if a string can be converted to a number
def checkIfNumber():
    tempInput = input()
    if tempInput.isdigit():
        return int(tempInput) #If the string is a number convert it to int and return it.
    else:
        print("The entered value is not a number. Please try again.")
        return checkIfNumber() #If it's not a number try again.
    
#Function for checking if a number is a correct type
def isAType():
    tempNumber = checkIfNumber()
    if tempNumber <= 6:
        return tempNumber
    else:
        print("The entered value is incorrect. Please try something else.")
        return isAType()



#Print the options
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponentiation")
print("6.Square Root")

while True:
    #Get input
    print("Enter the type of operation: ", end="")
    type = isAType()
    
    #Get the numbers for calculations
    print("Enter the first number: ", end="")
    firstNum = checkIfNumber()

    if type != 6:
        print("Enter the second number: ", end="")
        secNum = checkIfNumber()

    #Calculate
    if type == 1:
        print(firstNum + secNum)
    elif type == 2:
        print(firstNum - secNum)
    elif type == 3:
        print(firstNum * secNum)
    elif type == 4:
        print(firstNum / secNum, "or", firstNum // secNum, "and", firstNum % secNum, "remainder.")
    elif type == 5:
        print(firstNum ** secNum)
    else:
        print(sqrt(firstNum))

    #Sleep for half of a second, so the user can have enought time to see the answer
    sleep(0.5)

