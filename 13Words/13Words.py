def getUsersDecision():
    while True:
        option = input("Your decision: ")
        if option != "1" and option != "2":
            print("This is not an option. Please try again.")
        else:
            return option


def countWords(strText):
    words = 1
    # Count all spaces in the text
    for x in strText:
        if x == " ":
            words += 1
    return words


print("Please choose how would you like to enter the text.")
print("1. Write it here.\n2. Load it from a file.")

# Get the user's decision from a function
option = getUsersDecision()

# Declare text as a global variable
text = ""

# If the user wants to write the text
if option == "1":
    text = input("Enter the text: ")

# If the user wants to read the text from a file
if option == "2":
    path = input("Enter the file's path: ")

    # Check if the files exists
    try:
        with open(path, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File was not found.")
        exit()

# Print the outcome
print("This text has", countWords(text), "words.")

