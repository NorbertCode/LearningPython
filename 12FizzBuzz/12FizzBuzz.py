for x in range(1,100):
    #Declare a string
    strX = ""
    #If x is a multiple of 3 concatenate strX with "Fizz"
    if x % 3 == 0:
        strX += "Fizz"
    #If x is a multiple of 3 concatenate strX with "Buzz"
    if x % 5 == 0:
        strX += "Buzz"
    #If it's neither set strX to x
    if strX == "":
        strX = str(x)

    print(strX)
