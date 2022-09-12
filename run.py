from random import randint


class font_colour:
    RED = '\033[91m'
    GREEN = '\033[92m'
    WHITE = '\033[0m'


def menu_logo():
    """
    Main menu logo and game initialisation
    """
    print("""
 _     _                                   _  _____     __
| |   | |                                 ( )/ ___ \   / /
| |__ | | ____ ____   ____ ____   ____ ___|/( (   ) ) / /_
|  __)| |/ _  |  _ \ / _  |    \ / _  |  _ \ > > < < / __ \\
| |   | ( ( | | | | ( ( | | | | ( ( | | | | ( (___) | (__) )
|_|   |_|\_||_|_| |_|\_|| |_|_|_|\_||_|_| |_|\_____/ \____/
                    (_____|
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """)
    print("Would you like to play hangman?" + font_colour.GREEN +
          ' (y)es or (n)o:' + font_colour.WHITE)
    while True:
        answer = input()
        if answer.lower() == 'y':
            return rules()
        elif answer.lower() == 'n':
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
            """)
            exit()
        else:
            print(font_colour.RED + "Please enter a valid option" +
                  font_colour.WHITE)


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
    If your guess is correct, the letter will be displayed in its
    relevant position in the word.
    If your guess is incorrect, the hangman gallows will build up.
    You have 8 guesses.
    """)
    print('Do you want to continue?' + font_colour.GREEN +
          ' (y)es or (n)o:' + font_colour.WHITE)
    while True:
        answer = input()
        if answer.lower() == 'y':
            return set_difficulty()
        elif answer.lower() == 'n':
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
        """)
            exit()
        else:
            print(font_colour.RED + "Please enter a valid option" +
                  font_colour.WHITE)


def set_difficulty():
    """
    Asks player to set difficulty
    """
    print("\n")
    print(" Select your difficulty level:\n")
    print(font_colour.GREEN + " Press 1" + font_colour.WHITE +
          " for Level 1 - 4 letter word")
    print(font_colour.GREEN + " Press 2" + font_colour.WHITE +
          " for Level 2 - 6 letter word")
    print(font_colour.GREEN + " Press 3" + font_colour.WHITE +
          " for Level 3 - 8 letter word")
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


def get_random(difficulty):
    """
    Picks a random word to be used for the players guess from the
    answers.txt file
    """
    wordFile = open('answers.txt', 'r')
    words = wordFile.readlines()
    wordFile.close()

    return_list = []
    for word in words:
        if len(word) == difficulty + 1:
            return_list.append(word)

    return return_list[randint(0, len(return_list)-1)][0:-1]


def play(difficulty):
    """
    Play the game. Incorrect letters draw out the hangman
    until the image is complete and it is game over.
    """
    word = get_random(difficulty)
    progress = ''
    for i in range(len(word)):
        progress += '_'
    incorrect = 0
    letters = []
    while True:
        letterString = ''
        for i in range(len(letters)):
            if i != len(letters) and i != 0:
                letterString += ', '
            letterString += letters[i]
        print(draw_man(incorrect))
        print(f'Letters used: {letterString}')
        if progress == word:
            print(progress)
            print(user_wins())
            restart_game()
            break
        if incorrect >= 8:
            print(user_loses())
            print(f'The word was {word}.')
            restart_game()
            break
        print(progress)
        print(f'Number of incorrect guesses {incorrect}')
        print('Guess a letter!')
        user_input = input()
        if user_input not in letters and validate_guess(user_input):
            letters.append(user_input)
        if user_input in word:
            print(font_colour.GREEN + f'The letter {user_input} is in the'
                  ' word.' + font_colour.WHITE)
            for i in range(len(word)):
                if user_input == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + user_input + progressEnd
        elif validate_guess(user_input) is False:
            print(font_colour.RED + f'{user_input} is not a valid guess,'
                  'Please try again' + font_colour.WHITE)

        else:
            print(font_colour.RED + f'The letter {user_input} is not in the'
                  ' word. Please try Again.' + font_colour.WHITE)
            incorrect += 1


def validate_guess(guess):
    """
    Checks if user has inputted a number, symbol or more than 1 letter
    and returns an error message
    """
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        return False


def restart_game():
    """
    When game ends user to choose to restart the game or exit
    """
    while True:
        choice = input("Would you like to play again?" + font_colour.GREEN +
                       ' (y)es or (n)o:' + font_colour.WHITE)
        if choice == "y":
            main(False)
        elif choice == "n":
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
        """)
            exit()
        else:
            print(font_colour.RED + "Please enter a valid option" +
                  font_colour.WHITE)


def draw_man(incorrect):
    """
    Draws hangman gallow and stick figure in increments
    up to 8 until a complete hangman is drawn
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
    return("""
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
    return("""
 _     _  _____  _   _     _      _____  ___   _____
( )   ( )(  _  )( ) ( )   ( )    (  _  )(  _`\(_   _)
`\`\_/'/'| ( ) || | | |   | |    | ( ) || (_(_) | |
  `\ /'  | | | || | | |   | |  _ | | | |`\__ \  | |
   | |   | (_) || (_) |   | |_( )| (_) |( )_) | | |
   (_)   (_____)(_____)   (____/'(_____)`\____) (_)
   """)


def main(first_run):
    """
    Runs the game
    """
    difficulty = 6
    if first_run:
        print(draw_man(0))
    difficulty = menu_logo()
    play(difficulty)


main(True)
