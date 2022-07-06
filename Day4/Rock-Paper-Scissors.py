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

#Write your code below this line 👇
move = [rock,paper,scissors]
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
pc_move = random.randint(0,2)
if user_move == 0 :
  if pc_move == 0 :
    print(f"Draw! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 1:
    print(f"DAMN Loser!\n The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 2:
    print(f"Winner winner chiken dinner! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
    
elif user_move == 1:
  if pc_move == 0 :
    print(f"Winner winner chiken dinner! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 1:
    print(f"Draw!\n The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 2:
    print(f"DAMN Loser! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")

elif user_move == 2:
  if pc_move == 0 :
    print(f"DAMN Loser! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 1:
    print(f"Winner winner chiken dinner!\n The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
  elif pc_move == 2:
    print(f"Draw! The computer chose:\n {move[pc_move]}\n And you choose {move[user_move]}")
