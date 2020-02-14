def getUsersDecision(strQuestion, smallestNum, biggestNum):
    while True:
        strCategory = input(strQuestion)
        if strCategory.isdigit():
            # If the decision is between smallestNum and biggestNum
            if int(strCategory) < smallestNum or int(strCategory) > biggestNum:
                print("There is no such option. Please try again.")
            else:
                return strCategory
        else:
            print("This is not an option. Please try again.")


# Print the options
print("1. Units of temperature", "2. Units of currency", "3. Units of mass", "4. Units of distance",
      "5. Units of speed", sep="\n")

category = getUsersDecision("Which one of these do you want to convert? ", 1, 5)

# Declare units as a dictionary
units = { }

# Units of temperature
if category == "1":
    # Get the units and their values into a dictionary
    units = {
        # All of these are equal
        "Celsius": 1.0,
        "Kelvin": 274.15,
        "Fahrenheit": 33.8
    }

# Units of currency
if category == "2":
    # Get the units and their values into a dictionary
    units = {
        # All of these are equal
        "US Dollars": 1.0,
        "Canadian Dollars": 1.33,
        "Australian Dollars": 1.48,
        "Euros": 0.92,
        "Swiss Francs": 0.98,
        "British Pounds": 0.77,
        "Japanese Yens": 110.06
    }

# Units of mass
if category == "3":
    # Get the units and their values into a dictionary
    units = {
        # All of these are equal
        "Grams": 1000.0,
        "Kilograms": 1.0,
        "Tonnes": 0.001,
        "Ounces": 35.27,
        "Pounds": 2.2,
        "Short Tons": 0.0011
    }

# Units of distance
if category == "4":
    # Get the units and their values into a dictionary
    units = {
        # All of these are equal
        "Millimeters": 0.0001,
        "Centimeters": 0.01,
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Inches": 39.37,
        "Feet": 3.28,
        "Yards": 10.9,
        "Miles": 0.00062
    }

# Units of speed
if category == "5":
    # Get the units and their values into a dictionary
    units = {
        # All of these are equal
        "Meters per second": 0.28,
        "Kilometers per hour": 1.0,
        "Feet per second": 0.91,
        "Miles per hour": 0.62
    }

# Print the units to the user
num = 1
for x in units:
    print(str(num) + ".", x)
    num += 1

# Set toBeDecision to the number of the option chosen by the user and make toBeConverted the value of that option
toBeDecision = int(getUsersDecision("Which one of these do you want to convert? ", 1, num - 1))
toBeConverted = list(units.items())[toBeDecision - 1][1]

# Get the amount of the given unit
while True:
    try:
        value = float(input("Enter the number of " + list(units.items())[toBeDecision - 1][0] + " to convert: "))
        break

    except ValueError:
        print("The given input is not a number. Please try again")

# Set decisionTo to the number of the option chosen by the user and make convertedTo the value of that option
decisionTo = int(getUsersDecision("Which unit do you want to convert to? ", 1, num - 1))
convertedTo = list(units.items())[decisionTo - 1][1]
del num

result = 0
# If the users converts temperature units
if category == "1":
    if list(units.items())[toBeDecision - 1][0] == "Celsius":
        if list(units.items())[decisionTo - 1][0] == "Kelvin":
            result = value + 273.15

        elif list(units.items())[decisionTo - 1][0] == "Fahrenheit":
            result = value * 1.8 + 32

        else:
            result = value

    elif list(units.items())[toBeDecision - 1][0] == "Kelvin":
        if list(units.items())[decisionTo - 1][0] == "Celsius":
            result = value - 273.15

        elif list(units.items())[decisionTo - 1][0] == "Fahrenheit":
            result = value * 1.8 - 459.67

        else:
            result = value

    elif list(units.items())[toBeDecision - 1][0] == "Fahrenheit":
        if list(units.items())[decisionTo - 1][0] == "Celsius":
            result = (value - 32) / 1.8

        elif list(units.items())[decisionTo - 1][0] == "Kelvin":
            result = (value + 459.67) * (5 / 9)

        else:
            result = value

# If the user converts any other units
else:
    result = (convertedTo / toBeConverted) * value

# Round the result if it's not equal to 0
if not round(result, 2) == 0: result = round(result, 2)

# Print the outcome
print(value, list(units.items())[toBeDecision - 1][0], "is equal to ", end="")
print(result, list(units.items())[decisionTo - 1][0])
