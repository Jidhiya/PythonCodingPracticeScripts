userInput = input("Enter the letter :\n").lower()
if userInput in 'aeiou':
    print("User provided letter" , userInput, " is a Vowel")
else:
    print("User provided letter" , userInput, " is a Consonant")