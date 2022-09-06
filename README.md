# **Hangman'86**
Hangman'86 is a Python terminal game in which players can try to guess a randomly generated word by inputting letters, this runs on the Code Institute mock terminal on Heroku. The game is over when the player either guesses the word correctly or the maximum number of incorrect guesses has been reached and the hangman gallows image is completed. The target audience is developers working in the IDE who enjoy playing straight forward games in their downtime or fellow beginner coders looking for inspiration for their next challenge. 

[Hangman'86](https://hangman-86.herokuapp.com/) - The live site can be viewed here. 

![Am I Responsive?](docs/read-me/responsive.png) 

## **Table of Contents**
 * [**How to Play**](#how-to-play)
 * [**Planning Stage**](#planning-stage)
 * [**Features**](#features)
 * [**Testing**](#testing)
 * [**Technologies Used**](#technologies-used)
 * [**Bugs**](#bugs)
 * [**Validators**](#validators)
 * [**Deployment**](#deployment)
 * [**Credits**](#credits)

## **How to Play**
The game starts by prompting players to select a difficulty level which generates a random word of 4, 6 or 8 letters depending on the level chosen. Once the level has been selected the game initialises and players are prompted to input a letter in the terminal and press enter to play their guess. The goal of the game is to guess the hidden word, represented by _ _ _ _ relevant to the difficulty level chosen. Level 1 generates a 4 letter word, Level 2 a 6 letter word and Level 3 an 8 letter word. 
An error message is displayed if a player enters an incorrect command and is asked to resubmit a new guess. If the letter guessed is correct, the _ is replaced by the chosen letter in its relevant position in the word until all the letters are revealed and the game is over. If the letter guessed is incorrect a piece of the Hangman gallows is added to the terminal, players have a maximum of 8 incorrect guesses before the gallows is completed and the game is over.

## **Planning Stage**

### **User Experience UX**
To build a terminal version of Hangman for a developer to use in an IDE environment whilst taking a break from coding.
 * As a user, I want the game to be easy and fun to play.
 * As a user, I want clearly readable instructions on how the game works.
 * As a user, I want the game to provide a level of challenge without being too difficult.

 ## **Features**

 ### **Existing Features**
* Game Menu
  * Can select to start game to progress to rules menu
* Rules Menu
* Set Difficulty
