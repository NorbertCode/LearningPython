#A loop for checking if the user's input is a number
while True:
    print("How many number of the Fibonacci Sequence do you want? ", end="")
    tempNumber = input()
    if tempNumber.isdigit():
        amountOfNumbers = int(tempNumber)
        break
    else:
        print("This is not a correct number. Please try again.")

fibSequence = [0, 1, 1] #List of numbers
currentNumber = 0 #For checking how many numbers to print
tempFib = 0 #For checking which number from the list to pick

#Loop for calculating the sequence
while currentNumber < amountOfNumbers:
    if tempFib > 2:
        tempFib = 0

    print(fibSequence[tempFib])
    #Calculates the next number by adding all values from the list and removing the one that was just printed
    fibSequence[tempFib] = fibSequence[0] + fibSequence[1] + fibSequence[2] - fibSequence[tempFib]
    tempFib += 1
    currentNumber += 1
