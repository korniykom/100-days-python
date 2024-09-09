import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

your_move = input("Your move (0 - rock, 1 - paper, 2 - scissor)")
print(moves[int(your_move)])
computer_move = random.choice(moves)
print(computer_move)