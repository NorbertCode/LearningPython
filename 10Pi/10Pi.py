from math import pi

#Declare amount as a string and firstTime as a bool
amount = ""
firstTime = True
while not amount.isdigit():
    #Check if firstTime is false to make sure this message only shows when the user enters text
    if not firstTime: print("This is not a number. Try again.")
    firstTime = False
    amount = input("How many digits of Pi should be generated? The maximum is 14 decimal places\n")

strPi = str(pi)
#Print pi with the given amount of decimal places
print(strPi[0:int(amount) + 2])
