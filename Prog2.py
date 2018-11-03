### Program 2
### Ruben Morales Jr
### Number guessing game

### Import random

import random

#setting varibles to default
answer = "yes"
gamesWon = 0
totalGames = 0

#while loop to be able to play the game again if answer is yes
while answer == "yes":

    #counts total number of games and prints statements
    totalGames += 1
    print("I am thinking of a number in the range of 1-64 inclusive.")
    print(" You have 7 tries to guess it.")

    #generate a random number between 1 - 64
    randNumber = random.randint(1, 64)

    #for loop for tries
    for numberOfTries in range(8):
        
        #if number of tries is 7 then you lose
        if numberOfTries == 7:
            print("Sorry, you lose!! The number was", randNumber)
            break
        
        #else it keeps asking for guess
        else:
            guessNumber = int(input("What is your guess? "))

        #while loop to ask to try again if number is out of range
        while guessNumber < 1 or guessNumber > 64:
            guessNumber = int(input("Your guess was outside the range, try again. "))

        #if the guessing number is more than the randomized number, then guess is too high
        if guessNumber > randNumber:
            print("Sorry your guess was too high.")

        #if the guessing number is less than the randomized number, then guess is too low
        elif guessNumber < randNumber:
            print("Sorry your guess was too low")

        #else if guessing number is equal to randomized number, then player won
        #counts the number of games won
        else:
            print("Congrats, you are a winner in", numberOfTries, "tries!!")
            gamesWon += 1
            break

    #asks to play again or quits game if anything besides yes is inputted
    answer = input("Enter yes to play again, anything else to quit.")

#calculates the percentage and prints the stats for percentage of games won
percentage = (gamesWon / totalGames) * 100
print("You won ", gamesWon, "game(s) out of ", totalGames, "for a winning percent of "+format(percentage, ".3f")+"%")