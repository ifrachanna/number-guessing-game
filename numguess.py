
import random
target= random.randint(1,100)
print("Welcome to the number guessing game!")
while True:
    guess=int(input("Enter your guess (between 1 and 100): "))
    if guess<1 or guess>100:
        print("Please enter a number between 1 and 100.")
        continue
    elif guess==target:
        print("Congratulations! You've guessed the number!")
        break
    elif guess<target:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
print("Thank you for playing the number guessing game!")

