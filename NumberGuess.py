# Random number guessing game
import random

guesses = 0
print("I'm thinking of a number between 1 and 100.")
print("Try to guess the number in as few tries as possible.")

target = random.randint(1,100)
guess = 0

while guess != target:
    guess = int(input("Enter your guess:"))
    guesses +=1

    if guess < target:
        print("Too low!")
    if guess > target:
        print("Too high!")

print("Correct! The answer is " + str(target) + ".")
print("You got the answer in " + str(guesses) + " guesses.")
input("Press Enter to finish.")

