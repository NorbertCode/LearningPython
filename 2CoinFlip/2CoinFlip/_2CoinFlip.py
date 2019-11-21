import random #import a library
from time import sleep

while True: #The main loop.
    print("How many time do you want to flip a coin? ")
    tempInput = input()
    if tempInput.isdigit():
        flipAmount = int(tempInput) #Check if the input is a number and convert it to int
        #Setting up the variables for calculating
        tails = 0
        heads = 0
        total = 0

        #The loop
        for counter in range(0, flipAmount):
            total+=1
            #Randomize
            if random.randint(0,100) < 50:
                print("It's tails.")
                tails+=1
            else:
                print("It's heads.")
                heads+=1
            sleep(0.5) #After randomizing sleep for 0.5 seconds

        #Show the outcome
        print(tails, "out of", total, "were tails. That's " + str(tails / total * 100) + "%")
        print("Do you want to exit?")
        if(input().lower() == "yes"):
            break

    else:
        print("This is not a number. Please try again.")