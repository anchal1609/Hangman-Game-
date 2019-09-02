import random

Hangman = (
"""
-------
|     |
|     |
|
|
|
|
|
|
|
------------
""",
"""
-------
|     |
|     |
|     0 
|
|
|
|
|
|
------------
""",
"""
-------
|     |
|     |
|     0 
|    /|  
|    
|
|
|
|
------------
""",
    """
-------
|     |
|     |
|     0 
|    /|\ 
|      
|
|
|
|
------------
""",
"""
-------
|     |
|     |
|     0 
|    /|\  
|    /  
|
|
|
|
------------
""",
"""
-------
|     |
|     |
|     0 
|    /|\  
|    / \ 
|
|
|
|
------------
""",
)
alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
correctGuess = 0
wordList = []
word = []
with open("words.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word.append(line.split())
for i in word:
    for j in i:
        wordList.append(j)
li = iter(wordList)
t = len(wordList)
while (t>0):

    chosenWord = next(li)
    guess = None  # player guess input
    guessedLetters = []  # we add all the user guesses to this list
    blankWord = []  # replace all the letters of the chosen word with dashes
    for letter in chosenWord:
        blankWord.append("_")
    attempts = 6

    while attempts > 0:
        if(attempts !=0 and '_' in blankWord):
            print(("\nYou have {} attempts remaining.").format(attempts))
        try:
            print("\nLetter between A to Z: ")
            guess = random.choice(alphabet) #randoom number choosen by computer
            print("Guessed: ",guess)
        except:
            print("That is nt valid input!!")
            continue
        else:
            if not guess.isalpha():
                print("That is not a letter!! try again ;)")
            elif len(guess) > 1:
                print("Please enter one letter at a time!!")
                continue
            elif guess in guessedLetters:
                print("You have already guessed that letter! try diffrent letter;) ")
                continue
            else:
                pass

            guessedLetters.append(guess)

            if guess not in chosenWord:
                attempts-=1
                print(Hangman[(len(Hangman)-1)-attempts])
            else:
                searchMore = True
                startSearchIndex = 0
                while searchMore:
                    try:
                        foundAtIndex = chosenWord.index(guess, startSearchIndex)
                        blankWord[foundAtIndex] = guess
                        startSearchIndex = foundAtIndex + 1
                    except:
                        searchMore = False

            print(" ".join(blankWord))
            if attempts == 0:
                accuracy = round(100 - ((blankWord.count('_') / len(chosenWord)) * 100),2)
                if (blankWord.count('_') == 0):
                    correctGuess += 1;
                with open('results.txt', 'a') as file:
                        file.write("{} {}%\n" .format(chosenWord,accuracy))
                t = t-1
print("Thanks for playing...")
accuracyTotal = round((correctGuess/len(wordList))*100,2)
print("CorrectGuess: ",correctGuess)
print("Total Accuracy: ",accuracyTotal,"%")
