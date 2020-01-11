#Function used to reverse the word given as an argument
def reverse(word):
    #Set up variables
    letterNumber = 1
    reversedWord = ""
    #Loop to reverse the string
    while letterNumber < len(word) + 1:
        reversedWord += word[-letterNumber]
        letterNumber+=1

    return reversedWord

#Get user's input
word = input("Enter a word: ")
#Check if the word is a palindrome
if word == reverse(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

