from random import randint
from os import system


def menu_logo():
    """
    Main menu logo and game initialisation 
    """
    print("""
        
 /$$   /$$                                                                /$$ /$$$$$$   /$$$$$$ 
| $$  | $$                                                               | $//$$__  $$ /$$__  $$
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$|_/| $$  \ $$| $$  \__/
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$  |  $$$$$$/| $$$$$$$ 
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$   >$$__  $$| $$__  $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$  | $$  \ $$| $$  \ $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$$$/|  $$$$$$/
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/   \______/  \______/ 
                               /$$  \ $$                                                        
                              |  $$$$$$/                                                        
                               \______/                                                         

        """)
    print('Would you like to play hangman?  (yes/no)')
    answer = input()
    if answer.lower() == 'yes':
        rules()
        set_difficulty()
        play()
    if answer.lower() == 'no':
        print("""
            
 ..|'''.|                       '||  '||                       
.|'     '    ...     ...      .. ||   || ...  .... ...   ....  
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...|| 
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||      
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...' 
                                              .. |             
                                               ''              

            """)

def rules():
    """
    Displays the rules of the game before the game starts
    """
    print("""
    

  ____        _           
 |  _ \ _   _| | ___  ___ 
 | |_) | | | | |/ _ \/ __|
 |  _ <| |_| | |  __/\__ \\
 |_| \_\\__,_|_|\___||___/
                          
                                  

    Choose a letter and press enter to play your guess.
    If your guess is correct, the letter will be displayed in its relevant position in the word.
    If your guess is incorrect, the hangman gallows will build up. You have 8 guesses.
    """)
    print('Type yes to continue or no to end the game (yes/no)')
    answer = input()
    if answer.lower() == 'yes':
        set_difficulty()
        play()
    if answer.lower() == 'no':
        print("""
        
 ..|'''.|                       '||  '||                       
.|'     '    ...     ...      .. ||   || ...  .... ...   ....  
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...|| 
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||      
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...' 
                                              .. |             
                                               ''              
        """)

def set_difficulty():
    """
    Asks player to set difficulty
    """
    print("\n")
    print(" Select your difficulty level\n")
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

def getRandomWord():
    """
    Picks a random word to be used for the players guess from the answers.txt file
    """
    wordFile = open('answers.txt', 'r')
    words = wordFile.readlines()
    wordFile.close()
    return words[randint(0, len(words)-1)][0:-1]

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
        print(f'Number of incorrect guesses {incorrect}')
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
    if incorrect == 3:
        return """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 4:
        return """
        __________
        |/        |
        |         
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 5:
        return """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 6:
        return """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """
    if incorrect == 7:
        return """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """
    if incorrect == 8:
        return """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """    

def user_wins():
    """
    You Won logo displayed when player wins game
    """
    print("""

 _     _  _____  _   _     _       _  _____  _   _ 
( )   ( )(  _  )( ) ( )   ( )  _  ( )(  _  )( ) ( )
`\`\_/'/'| ( ) || | | |   | | ( ) | || ( ) || `\| |
  `\ /'  | | | || | | |   | | | | | || | | || , ` |
   | |   | (_) || (_) |   | (_/ \_) || (_) || |`\ |
   (_)   (_____)(_____)   `\___x___/'(_____)(_) (_)
                                                   
                                                   
   
""")

def user_loses():
    """
    You Lost logo displayed when player loses game
    """
    print("""

 _     _  _____  _   _     _      _____  ___   _____ 
( )   ( )(  _  )( ) ( )   ( )    (  _  )(  _`\(_   _)
`\`\_/'/'| ( ) || | | |   | |    | ( ) || (_(_) | |  
  `\ /'  | | | || | | |   | |  _ | | | |`\__ \  | |  
   | |   | (_) || (_) |   | |_( )| (_) |( )_) | | |  
   (_)   (_____)(_____)   (____/'(_____)`\____) (_)  
                                                     
                                                     

    """)

def main():
    """
    Runs the game
    """
    print(drawMan(0))
    menu_logo()
    set_difficulty()
    getRandomWord()
    play()


main()