#CTI-110
#NELSONN
#MR.NORRIS
#M6HW2_Guessing Game



#import random(to be able to use call random.randint)
import random

#what is the highest and lowest numbers used

MIN = 1
MAX = 100

def play():
    #again = 'y'
    SecretNumber = random.randint(MIN, MAX)
    #print("Secret Number:",SecretNumber)
    guesses = 5
    while guesses > 0:
        Guess = int(input("Guess what the secret number is:"))
        if Guess > SecretNumber:
            print('Too high, try again')
            guesses = guesses - 1
        elif Guess < SecretNumber:
            print('Too low, try again')
            guesses = guesses - 1
        elif Guess == SecretNumber:
            print('YOU GOT IT!')
            guesses = 0
def main():
    again = 'y'
    while again == 'y' or again == 'Y' or again == 'yes':
        play ()        
        again = input('Play again? (y = yes): ')
    
            
            
        
        
        
        
        
    
    
    
    

















main()
