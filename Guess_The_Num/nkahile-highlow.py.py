#NOUR KAHILE
#This program generate a random number,
#and gives you an infinite tries to guess it,
#and tells you if it's too low, too high, or guessed correctly.
import random
userNumber = random.randint(1,100)
print ("I'm thinking of a number between\n")
print ("1 and 100. Guess a number, and I'll tell you\n")
print ("if you're too high, too low, or got it right.\n")
guess = int (input("Go ahead and enter a number!: "))
numOfguesses = 1
while numOfguesses != 'guess':
    numOfguesses = int(numOfguesses) + 1
    if guess < userNumber:
        print ("too low!")
        guess = int (input("please enter a number from 1 to 100: "))
    elif guess > userNumber:
        print ("too high!")
        guess = int (input("please enter a number from 1 to 100: "))
    else:
        print ("you got it!")
        break
    if guess == userNumber:
        numOfguesses = str(numOfguesses)
        print("it took " +numOfguesses, "truns")