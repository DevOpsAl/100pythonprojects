'''
Created on Jul 25, 2022

@author: devopsadmin
'''
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

#Write your code below this line 👇

def game():
  #imports
  import random
  import sys
  
  #loop play
  def reset():
    restart = input("Play Again? (y/n)")
    if restart == "y" or restart == "Y":
      print("Starting New Game!")
      game()
    elif restart == "n" or restart == "N":
        sys.exit(0)
      
  print("""Welcome to Rock Paper Scissors!!
       The game is very simple. You choose either rock, paper, or scissors. The computer will randomly choose between the three. Rock beats scissors. Scissors beats paper. Paper beats rock.
""")
  
  #player choice
  player = int(input("""Which will you choose:
  1 for Rock
  2 for Scissors
  3 for Paper
  """))
  print()
  
  #computer choice
  cpu = random.randrange(1,4)
  
  #comparing choices
  #player = 1
  if player == 1 and cpu == 1:
    print(f"Player\n{rock}\n vs\n\n CPU\n{rock}")
    print("It's a tie!")
    reset()
  elif player == 1 and cpu == 2:
    print(f"Player\n{rock}\n vs\n\n CPU\n{scissors}")
    print("Rock vs Scissors\nYOU WIN!!!")
    reset()
  elif player == 1 and cpu == 3:
    print(f"Player\n{rock}\n vs\n\n CPU\n{paper}")
    print("Rock vs Paper\nYOU LOSE!!!")
    reset()

  #player = 2
  if player == 2 and cpu == 1:
    print(f"Player\n{scissors}\n vs\n\n CPU\n{rock}")
    print("Scissors vs Rock\nYOU LOSE!!!")
    reset()
  elif player == 2 and cpu == 2:
    print(f"Player\n{scissors}\n vs\n\n CPU\{scissors}")
    print("It's a tie!")
    reset()
  elif player == 2 and cpu == 3:
    print(f"Player\n{scissors}\n vs\n\nCPU{paper}")
    print("Scissors vs Paper\nYOU WIN!!!")
    reset()

  #player = 3
  if player == 3 and cpu == 1:
    print(f"Player\n{paper}\n vs\n\n CPU\n{rock}")
    print("Paper vs Rock\nYOU WIN!!!")
    reset()
  elif player == 3 and cpu == 2:
    print(f"Player\n{paper}\n vs\n\n CPU\n{scissors}")
    print("Paper vs Scissors\nYOU LOSE!!!")
    reset()
  elif player == 3 and cpu == 3:
    print(f"Player\n{paper}\n vs\n\n CPU\n{paper}")
    print("It's a tie!")
    reset()
  

game()