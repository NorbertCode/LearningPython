print("To exit the application type something and press enter.")
#Printing the first prime number
print("The first prime number is 2")
#Declaring global variables
strInput = ""
primeNum = 2
primeNumbers = [11]
#If the user types something it exits the program
while strInput == "":
    #Get the users input and set wasShown to false
    strInput = input("Do you want to see the next prime number? Press enter if you do.\n")
    wasShown = False

    #Check if a number is prime and if it isn't it iterates primeNum and check again.
    while not wasShown:
        #Set isPrime to true and iterate primeNum
        isPrime = True
        primeNum += 1

        #Checks if primeNum is divisible by any number between 2 and 10 or any of the prime numbers
        for x in (list(range(2, 10)) + primeNumbers):
            if primeNum % x == 0:
                if primeNum != x:
                    #If it's not a prime number break the loop
                    isPrime = False
                    break

        #If it's a prime number print it and add it to the list
        if isPrime:
            print("The next prime number is", primeNum)
            wasShown = True
            if primeNum > 10: primeNumbers.append(primeNum)
