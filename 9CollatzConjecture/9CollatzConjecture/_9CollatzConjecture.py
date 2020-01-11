#Function for checking if a string can be converted to a number
def checkIfNumber():
    tempInput = input()
    if tempInput.isdigit():
        return int(tempInput) #If the string is a number convert it to int and return it.
    else:
        print("The entered value is not a number. Please try again.")
        return checkIfNumber() #If it's not a number try again.


#Get the user's input and check if it's bigger than 1
startingNum = 0
while startingNum <= 1:
    print("Enter a number: ", end="")
    startingNum = checkIfNumber()
    if startingNum <= 1:
        print("The number has to be bigger than one.")


#Do the Collatz Conjecture process
Steps = 0
while startingNum != 1:
    if startingNum % 2 == 0: #If the number is even divide by 2
        startingNum /= 2
    else: #If the number is odd multiply by 3 and add 1
        startingNum = startingNum * 3 + 1
    #Add one step
    Steps+=1


#Print the outcome
print("The process reached one in", Steps, "steps.")

