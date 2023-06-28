import random
import csv

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                  # initial empty state
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def hangman():
    print("Choose an option to select the genre of words")
    print("1.Sports \n2.Food \n3.Places")
    choices={1:"sports"  , 2:"food" , 3:"places"}
    genre=int(input('Enter your choice : '))
    print('')
    if genre in choices.keys():
        with open('Hangman.csv','r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for line in csv_reader:
                if choices[genre]==line[0]:
                    word=random.choice(line[1:])
    else:
        print("Enter a valid data :")

    tries=7
    guessmade=""
    letter_used=list()
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    def update():
        if guess in valid_entry:
            valid_entry.remove(guess)
            letter_used.append(guess)

    while len(word)>0 and tries>0:
        main_word=''
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+'_ '   

        if main_word == word:
            print('')
            print("---------------------")
            print(main_word,'!')
            print("You Won",name,"!!")
            print("---------------------")
            break
        print('')
        print(display_hangman(tries))
        print('Letters used are : ',letter_used)
        print("Guess the word ",main_word)
        guess=input("Enter the letter: ") 
        if guess not in word:
            tries -= 1 
        while True:
            if guess in valid_entry:
                guessmade=guessmade+guess
                update()
                break
            else:
                print('')
                print("Enter a valid character")
                guess=input("Enter the letter: ")
        if tries==1:
            print('\nONLY 1 CHANCE LEFT\nSAVE AN INNOCENT MAN FROM DYING!!!\n')
        elif tries==0:
            print(display_hangman(0))
            print('\nYOU LOSE ',name,'\nBETTER LUCK NEXT TIME :(')
choice='y'              
while choice=='y':
  print("WELCOME TO HANGMAN!")
  name = input("Enter your Name : ")
  print('')
  print("----------------------------")
  print("Welcome to Hangman",name,"!")
  print("Try to guess the word in less than 7 attempts")
  print("----------------------------")
  print('')
  hangman()
  choice=input("\nDo you wish to play again (y/n) : ")
