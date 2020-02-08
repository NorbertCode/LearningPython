for x in range(1,100):
    strX = ""
    if x % 3 == 0:
        strX += "Fizz"
    if x % 5 == 0:
        strX += "Buzz"
    if strX == "":
        strX = str(x)

    print(strX)
