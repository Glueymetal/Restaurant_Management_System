# JUMBLED WORDS

## 09 July 2024

### **Video Demo**:  <https://youtu.be/nKH7509Iaig>

### Hello! I am Jeyashree M. and This is my Final Project for CS50's Introduction to Programming with Python Course.

## **Description**:

## **Overview**:
    * My Project called "Jumbled Words" is a command-line interface game where the user can choose any one of the modes and rearrange the jumbled words to their actual spelling

    * User can progress to the next mode after clearing the current mode or exit the game at any part of the program.

## **Requirements**
    * Prerequisites before running the Jumbled Words Game
        + Python 3.x
        + modules - random,sys,pillow.

### **Project Structure:**
## ***1. final.py***

**Main Function - def main():**

    + The main function serves as a entry point for the game.

    + It allows the users to interact with program by displaying the title and modes of difficuilties to choose form

    + The Chosen mode undergoes verification using the verifymode() function

    + Using Conditional Statements,the program call for the specific functions which returns the score and then calls for another function for progressing through the modes or exit the program if user had asked for it.

**def verifymode()**

    Returns the mode if one of the specified modes is given or raises ValueError which is caught by the main and ends the program using 'sys.exit'

## Game Modes:

**1.Easy Mode**
    + In this mode,the user receive 5 chances to guess the right answer.

    + They are given 5 questions for the category they choose from.

    + Categories provided:Colours and Animals.

    + If the user does not answer within the attempts,the program shows the correct answer and the next question is shown in the terminal.

    + If the user wishes to exit,they can by entering the "x".

**2.Medium Mode**
    + In this mode,the user receive 3 chances to guess the right answer.

    + They are given 5 questions for the category they choose from.

    + Categories provided:Common Elements in the Periodic Table and Iconic Dishes Around The World.

    + If the user does not answer within the attempts,the program shows the correct answer and the next question is shown in the terminal.

    + If the user wishes to exit,they can by entering the "x".

**3.Hard Mode**
    + In this mode,the user receive 1 chance to guess the right answer.

    + They are given 5 questions for the category they choose from.

    + Categories provided:Countries in Asia and Sports.

    + If the user does not answer within the attempts,the program shows the correct answer and the next question is shown in the terminal.

    + If the user wishes to exit,they can by entering the "x".

## Word Selection And Scrambling Logic:
### Working:

    + This applied in the functions : easy(), medium() and hard().
    + Users select a partcular category
    + The game access the category using the conditionals
    + Maintain a list of words related to the category
    + Use random.choice() to randomly select a word
    + Check the chosen word is already selected using the set called prev()
    + If not,add to the set
    + The selected word is made into a list and shuffled using random.shuffle()
    + The list is added back into a word and is presented to the user.
    + This is put in a While loop and it generates 5 questions as only less than 5 is mentioned.
    + The score is kept track and returned as soon as the user finshes the questions.

## Scoring and Progression:
        The following functions show how the program progresses to the next mode and how it show the scores to the user.

**def show_scores()**

    + The function has the arguments:mode,score.

    + Based on the mode and score obtained,the function returns the strings that tells the result.

**def restart()**

    + The function take argument:True or False.

    + For the argument True,the function calls for the main() function.

    + For False,it exits the program using sys.exit().

**def progress()**

    + This function helps the program to progress to the other modes and to exit the program in between.

    + This function works on the conditionals and calling for the easy(),medium() or hard() function.

    + This function works by two arguments:mode,score.

    + So,if the user scored 5 in any of the modes(easy or medium),then the user can progress to the next mode or user will be stuck on the same mode or exit the program through the one of the options.

    + If the user clears the hard mode with the score being 5, they get a image popup of medal with the line "winner" with help of image.show in the Image class in PIL library.

## ***2. test_final.py ***

    + This program is used to test some of the functions.

    + I have tested only the invalid values for the easy(),medium(),hard() functions due to the randomness of the questions.

    + I have checked using pytest whether my program raises ValueError and SystemExit properly.


## Conclusion:

    + Thank You for taking The time to read through my README file for my CS50P Final Project - Jumbled Words.

### **THANK YOU !!**






