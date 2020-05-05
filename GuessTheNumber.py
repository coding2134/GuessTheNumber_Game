import random

NumberOfGuesses = 7

print("Welcome to the game Guess a Number!")
print("Rules:You have 8 tries to guess the correct number, we'll tell you if your answer is too high or too low, Good Luck!")

number = random.randrange (1, 100)
guess = int(input("Guess a number between 1 and 100:"))

while NumberOfGuesses > 0:

    if guess < number:   
        GuessesLeft = str(NumberOfGuesses)
        print("That was too low. Try again.   Guesses Left: " + str(NumberOfGuesses)) 
        guess = int(input("Guess:"))
    elif guess > number:
        GuessesLeft = str(NumberOfGuesses)
        print("That was too High. Try again.  Guesses Left: " + str(NumberOfGuesses)) 
        guess = int(input("Guess:"))

    elif guess == number:
        print("Congrats, you have guessed the correct number.") 
        break
    else:
        print("Sorry, you input was invalid.")
        
    NumberOfGuesses = NumberOfGuesses - 1

    if NumberOfGuesses == 0:
        print("Sorry, you Lose. You ran out of guesses. The correct number was ", number)
    