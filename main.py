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
import random
x = True

print("Lets play Rock Paper Scissors!")
choice = input("Enter your choice!\n")
choice1 = choice.lower()
#while x == True:
#  if choice1 != "rock" or choice1 != "paper" or choice1 != "scissors":
#    print("Must choose rock, paper, or scissors!")
#    choice = input("Try again!\n")  
#    choice1 = choice.lower()
# x = False
    
options = ["rock", "paper", "scissors"]
comp_choice = random.randint(0,2)
choice2 = options[comp_choice]
choice2 = choice2.lower()

if choice1 == "rock" and choice2 == "rock":
  print(rock,rock)
  print("You both chose rock its a draw.\n")


if choice1 == "rock" and choice2 == "paper":
  print(rock,paper)
  print("The computer chose paper YOU LOSE :( .\n")


if choice1 == "rock" and choice2 == "scissors":
  print(rock,scissors)
  print("Rock beats scissors! YOU WIN!.\n")


if choice1 == "paper" and choice2 == "paper":
  print(paper,paper)
  print("You both chose paper its a draw.\n")


if choice1 == "paper" and choice2 == "scissors":
  print(paper,scissors)
  print("The computer chose scissors YOU LOSE :( .\n")

if choice1 == "paper" and choice2 == "rock":
  print(paper,rock)
  print("Paper beats rock! YOU WIN!.\n")

if choice1 == "scissors" and choice2 == "scissors":
  print(scissors,scissors)
  print("You both chose paper its a draw.\n")

if choice1 == "scissors" and choice2 == "paper":
  print(scissors,paper)
  print("The computer chose paper..YOU WIN! :( .\n")

if choice1 == "scissors" and choice2 == "rock":
  print(scissors,rock)
  print("Rock beats scissors..YOU LOSE!.\n")