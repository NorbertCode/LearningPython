#A function for checking if a word starts with a vowel.
def checkIfVowel(str):
    if str.startswith("a") or str.startswith("e") or str.startswith("i") or str.startswith("o") or str.startswith("u"):
        return True
    else:
        return False

#A function for checking if the user wants to close the program.
def checkIfClosing():
    print("Do you want to close the program?")
    if input().lower() == "yes":
        return True
    else:
        return False


#The main loop.
while True:

    #Have the user input a word.
    print("Write a word in English: ", end="")
    word = input()

    startsWithVowel = False

    #If the word starts with a vowel add way to the end.
    if checkIfVowel(word):
        word = word + "way"
        print("The word in Pig Latin is " + word)

        #Check if the user wants to close the program.
        if checkIfClosing():
            break

    #If the word doesn't start with a vowel move every consonant to the end.
    else:
        while not checkIfVowel(word):
            word = word[1:] + word[0]

        #Add "ay" to the end.
        word+="ay"
        print("The word in Pig Latin is " + word)

        #Check if the user wants to close the program.
        if checkIfClosing():
            break

