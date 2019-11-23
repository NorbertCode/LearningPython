def checkIfNumber(whatToPrint):
    print(whatToPrint, end="")
    tempInput = input()
    if tempInput.isdigit():
        return float(tempInput) #If the string is a number convert it to float and return it.
    elif tempInput.count(".") > 0 and tempInput.count(".") < 2:
        return float(tempInput) #If it's a floating point number convert it and return it.
    else:
        print("The entered value is not a number. Please try again.")
        return checkIfNumber(whatToPrint) #If it's not a number try again.
        


while True:
    #Set the variables
    cost = checkIfNumber("The item's cost: ")
    money = checkIfNumber("The amount of money you have: ")

    if money < cost:
        print("You don't have enough money.")
    else:
        #Count the change
        change = round(money - cost, 2)
        print("The change is", change, "which can be paid in:")

        #Define some variables
        dollars = 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        #Count the amount of dollars, quarters, dimes, nickels and pennies
        while change >= 1:
            dollars+=1
            change-=1

        while change >= 0.25:
            quarters+=1
            change-=0.25

        while change >= 10:
            dimes+=1
            change-=0.10

        while change >= 0.05:
            nickels+=1
            change-=0.05

        while change > 0:
            pennies+=1
            change-=0.01

        #Print the values
        print("Dollars:", dollars)
        print("Quarters:", quarters)
        print("Dimes:", dimes)
        print("Nickels:", nickels)
        print("Pennies:", pennies)



    
