# You could just use selenium to open a website that calculates the distance, but this I wanted to do it the hard way
# so I made it get the coordinates of places and calculate it using that.

from selenium import webdriver
from bs4 import BeautifulSoup
from math import radians, cos, sin, asin, sqrt


def getCoordinatesFromText(strCoordinates):
    # Declare variables needed to get the coordinates from the text
    strLat = ""
    strLong = ""
    isLatFinished = False  # Helps to differentiate Latitude from Longitude
    wasLastCharNum = False

    # Help to check if it should stop adding numbers to strLong
    wasDot = False
    charsAfterDot = 0

    # Loop through the text and find the coordinates
    for x in strCoordinates:
        # Getting the latitude
        if not isLatFinished:
            if not wasLastCharNum:
                if x.isdigit() or x == ".":
                    strLat += x
                    wasLastCharNum = True

            else:
                if x.isdigit() or x == ".":
                    strLat += x

                else:
                    isLatFinished = True

        # Getting the longitude
        elif isLatFinished and (x.isdigit() or x == "."):
            if x == ".":
                wasDot = True

            if wasDot:
                charsAfterDot += 1

            if charsAfterDot > 7:
                break
            else:
                strLong += x

    try:
        return float(strLat), float(strLong)
    except ValueError:
        print("Could not find the location.")
        input()
        exit()


# Make it so Chrome doesn't pop up
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Open chrome and search for the coordinates of the first place
strFirstPlace = input("What's the first place? ")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/search?q=" + strFirstPlace + "+coordinates")

# Search for the coordinates on the page
soupSource = BeautifulSoup(driver.page_source, features="html.parser")
coordinates = soupSource.find("span", attrs={"class": "e24Kjd"})
strCoordinates = str(coordinates)[21:-1]

flLat1, flLong1 = getCoordinatesFromText(strCoordinates)


# Search for the coordinates of the second place
strSecondPlace = input("What's the second place? ")
driver.get("https://www.google.com/search?q=" + strSecondPlace + "+coordinates")

# Search for the coordinates on the page
soupSource = BeautifulSoup(driver.page_source, features="html.parser")
coordinates = soupSource.find("span", attrs={"class": "e24Kjd"})
strCoordinates = str(coordinates)[21:-1]

flLat2, flLong2 = getCoordinatesFromText(strCoordinates)

# Close the driver
driver.close()

# Calculate the distance
flLat1 = radians(flLat1)
flLong1 = radians(flLong1)

flLat2 = radians(flLat2)
flLong2 = radians(flLong2)

dLat = flLat2 - flLat1
dLong = flLong2 - flLong1

a = sin(dLat / 2) ** 2 + cos(flLat1) * cos(flLat2) * sin(dLong / 2) ** 2
c = 2 * asin(sqrt(a))

print("The distance between", strFirstPlace, "and", strSecondPlace, "is", str(c * 6371), "km.")
