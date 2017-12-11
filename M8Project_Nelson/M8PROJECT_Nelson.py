#Najah Nelson
#Cti-110
#Python Game

import random
words = ""
right_letters = ""
wrong_letters = ""
#define what you want to do
def main():
    #what do I want my game to do?
    words = random_words()
    #what order do I want it to happen?
    start_game(words)
    #what happens if they win/lose?
    play_again()

#make a variable to define the file you want to open.
#how to point to my file pg.239, 6.1
#what keeps them from cheating and changing the answers? pg.239
#(it keeps printing all on one line!!!!..ugh)
#yayaya pg.247
#tell it to do the first portion, starting the game
#n=najah
#define the words
def random_words():
    n = open("answers.txt", "r")
    SelectLine = random.randint(0,9)
    for line in range(SelectLine):
#pg.247
        words = n.readline()
        words = words.rstrip()
#what comman is going to give me what I ask for?
    return words


#we found the file to execute now what?
#use the secret number hw
#define SecretWords
def start_game(SecretWords):
    #use true or false statements
    YouLose = False
    while YouLose == False:
        #what you see
        show_table(SecretWords)
        #start trying the game
        attempt = input_attempt ()
        #how do you know?
        YouLose = check_attempt(attempt, SecretWords)
        #continue until you win or you lose
        #Be done
#define show_table
#inventwithpython CH.9
def show_table(words):
    print("Wrong Letters: ", end=' ')
    for letters in wrong_letters:
        print(letters, end=" ")

    print()
    blanks = "_" * len(words)

    for i in range (len(words)):
        if words[i] in right_letters:
            blanks = blanks[:i] + words[i] + blanks [i+1:]
    for letter in blanks:
            print (letter, end=" ")
    print()
#define input_attempt
#ch. 9, make sure its only one letter at a time, make sure its a letter.

def input_attempt():
    good_attempt = False
    while good_attempt == False:
        print('Guess a letter.')
        attempt = input ()
        attempt = attempt.lower()
        if len(attempt) != 1:
            print('Please enter ONLY one letter.')


        elif attempt not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter letters ONLY.')

        else:
            good_attempt = True

    return attempt
        

#define check_attempt
#ch. 9, check flase and true statements

def check_attempt(attempt, words):
    #how can I get the words I picked not to change as varibles
    # pg. 193, 5.6, Global Constant
    global wrong_letters
    global right_letters
    YouLose = False

    if attempt in words:
        #if they get they get it right
        right_letters = right_letters + attempt

        guess_all = True
        for i in range (len(words)):
            if words[i] not in right_letters:
                guess_all = False

        if guess_all:
            print("You did it! The right answer is: ", words, "GOOD JOB!")
            YouLose = True


#define the wrong guesses
    else:
        wrong_letters = wrong_letters + attempt
        if len(wrong_letters) > 5:
                  print("NICE TRY! \n After" + str(len(wrong_letters)) + " failed attempts and " + str(len(right_letters)) + "correct attempts. The word was'" + words + " '.")
                  YouLose = True
    return YouLose

#continue to play or quit
#define play again
#pg. 193
#inventwithpython
def play_again():
    global right_letters
    global wrong_letters
    answer = input("Do you want to play again? [Y/N] ")
    if answer == 'y' or answer == 'Y':
        right_letters = ""
        wrong_letters = ""
        main()

    else:
        print("\n")
        print("Thank You, For your participation!")
        return False


  
main()                  
     
            
        





















