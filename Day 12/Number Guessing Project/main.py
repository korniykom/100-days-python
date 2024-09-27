import random

print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose difficulty. Type 'easy' or 'hard'\t")

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

random_number = random.randint(0, 100)
print(random_number)

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number. ")
    guess = input("Make a guess: ")
    if int(guess) == random_number:
        print(f"You got it! The answer was {random_number}")
        break
    if int(guess) < random_number:
        print("Too low")
    if int(guess) > random_number:
        print("Too high")
    if attempts > 1:
        print("Guess again")
    attempts -= 1
