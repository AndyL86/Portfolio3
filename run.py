from random import randint
from os import system

def getRandomWord():
    """
    Picks a random word to be used for the players guess from the answers.txt file
    """
    wordFile = open('answers.txt', 'r')
    words = wordFile.readlines()
    wordFile.close()
    return words[randint(0, len(words)-1)][0:-1]

def menu_logo():
    """
    Main menu logo and game initialisation 
    """
    print("Hangman'86")
    answer = input()
    if answer.lower() == 'yes':
        set_difficulty()
        play()
    if answer.lower() == 'no':
        print("Goodbye")

def set_difficulty():
    """
    Asks player to set difficulty
    """
    print("\n")
    print(" Select your difficult level\n")
    print(
        " Press 1 for Level 1, 4 letter word"
        )
    print(
        " Press 2 for Level 2, 6 letter word"
        )
    print(
        " Press 3 for Level 3, 8 letter"
        )
    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "1":
            difficulty = True
            letter_count = 4
            return letter_count
        elif options == "2":
            difficulty = True
            letter_count = 6
            return letter_count
        elif options == "3":
            difficulty = True
            letter_count = 8
            return letter_count
        else:
            print("\n Please select 1, 2 or 3 to make your choice")

def play():
    """
    Play the game. Incorrect letters draw out the hangman until the image is complete and it is game over.
    """
    word = getRandomWord()
    progress = ''
    for i in range(len(word)):
        progress += '_'
    incorrect = 0
    letters = []
    while True:
        _ = system('clear')
        lettersString = ''
        for i in range(len(letters)):
            if i != len(letters) and i != 0:
                lettersString +=', '
            lettersString += letters[i]
        print(drawMan(incorrect))
        print(f'Letters used: {lettersString}')
        if progress == word:
            print(progress)
            print(user_wins())
            break
        if incorrect >= 8:
            print(user_loses())
            print(f'The word was {word}.')
            break
        print(progress)
        print('Guess a letter!')
        print(f'Nmber of incorrect guesses {incorrect}')
        userInput = input()
        if userInput not in letters:
            letters.append(userInput)
        if userInput in word:
            print(f'The letter {userInput} is in the word.')
            for i in range(len(word)):
                if userInput == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + userInput + progressEnd
        else:
            print(f'The letter {userInput} is not in the word. Try Again.')
            incorrect += 1

def drawMan(incorrect):
    """
    Draws hangman gallow and stick figure in increments up to 7 until a complete hangman is drawn 
    """
    if incorrect == 0:
        return """





        
        """
    if incorrect == 1:
        return """
        |
        |
        |
        |
        |
        ========
        """
    if incorrect == 2:
        return """
        |/
        |
        |
        |
        |
        |\\
        ========
        """
    
    

def user_wins():
    """
    You Win! logo displayed when player wins game
    """
    print('You Win!')

def user_loses():
    """
    You Lose! logo displayed when player loses game
    """
    print('You Lose!')

def main():
    """
    Runs the game
    """
    print(drawMan(0))
    menu_logo()
    set_difficulty()

    game_word = getRandomWord()
    play()


main()