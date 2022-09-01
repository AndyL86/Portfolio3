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