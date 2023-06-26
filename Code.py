import random
import csv
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

    turns=10
    guessmade=""
    letter_used=list()
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    def update():
        if guess in valid_entry:
            valid_entry.remove(guess)
            letter_used.append(guess)

    while len(word)>0:
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
        print('Letters used are : ',letter_used)
        print("Guess the word ",main_word)
        guess=input("Enter the letter: ")     

        while True:
            if guess in valid_entry:
                guessmade=guessmade+guess
                update()
                break
            else:
                print('')
                print("Enter a valid character")
                guess=input("Enter the letter: ")

        if guess not in word:
            turns = turns-1
            if turns==9:
                print("")
                print("9 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
            if turns==8:
                print("")
                print("8 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("    O    ")
            if turns==7:
                print("")
                print("7 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("    O    ")
                print('    |    ')
            if turns==6:
                print("")
                print("6 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("    O    ")
                print('    |    ')
                print('   /     ')
            if turns==5:
                print("")
                print("5 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("    O    ")
                print('    |    ')
                print('   / \   ')
            if turns==4:
                print("")
                print("4 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("    O    ")
                print('    |    ')
                print('   / \   ')
            if turns==3:
                print("3 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("  \ O    ")
                print('    |    ')
                print('   / \   ')
            if turns==2:
                print("")
                print("2 TURNS LEFT!")
                print("HANGMAN:")
                print('---------')
                print("  \ O /   ")
                print('    |    ')
                print('   / \   ')
            if turns==1:
                print("")
                print("1 TURN LEFT , SAVE AN INNOCENT MAN FROM HANGING!")
                print("HANGMAN:")
                print('---------')
                print("  \ O /__|   ")
                print('    |    ')
                print('   / \   ')
            if turns==0:
                print("")
                print("----------------------------")
                print("You lose :(")
                print("Better luck next time!")
                print('The word was',word.upper())
                print("----------------------------")
                print("")
                break
choice='y'              
while choice=='y':
  print("WELCOME TO HANGMAN!")
  name = input("Enter your Name : ")
  print('')
  print("----------------------------")
  print("Welcome to Hangman",name,"!")
  print("Try to guess the word in less than 10 attempts")
  print("----------------------------")
  print('')
  hangman()
  choice=input("Do you wish to play again (y/n) : ")
