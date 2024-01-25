# Hangman Game

Welcome to the Hangman game! This is a simple on-terminal implementation in Python.

## How to Play

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/jainanjaly/Hangman.git
    ```

3. Run the game:

    ```bash
    python Code.py
    ```

4. Follow the on-screen instructions to guess the word.

## Features

- Provides user a with a list of categories to choose the word from.
- Randomly selects a word for the player to guess from the chosen category..
- Tracks and displays the correct guesses, incorrect guesses, and remaining attempts.
- Provides feedback on the game outcome (win or lose).

## Requirements

- Python 3.x

## Setup

No additional setup is required. Just clone the repository and run the game!

## Sample Gameplay

```plaintext
WELCOME TO HANGMAN!
Enter your Name : Anjaly 

----------------------------
Welcome to Hangman Anjaly  !
Try to guess the word in less than 7 attempts
----------------------------

Choose an option to select the genre of words
1.Sports 
2.Food 
3.Places
Enter your choice : 1



                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  []
Guess the word  _ _ _ _ _ _ _ 
Enter the letter: a


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a']
Guess the word  _ _ _ _ _ _ _ 
Enter the letter: o


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o']
Guess the word  _ o_ _ _ _ _ 
Enter the letter: l


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o', 'l']
Guess the word  _ o_ l_ _ _ 
Enter the letter: g


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o', 'l', 'g']
Guess the word  _ o_ l_ _ g
Enter the letter: i


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o', 'l', 'g', 'i']
Guess the word  _ o_ li_ g
Enter the letter: n


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o', 'l', 'g', 'i', 'n']
Guess the word  _ o_ ling
Enter the letter: b


                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
Letters used are :  ['a', 'o', 'l', 'g', 'i', 'n', 'b']
Guess the word  bo_ ling
Enter the letter: w

---------------------
bowling !
You Won Anjaly  !!
---------------------

Do you wish to play again (y/n) : nd!



