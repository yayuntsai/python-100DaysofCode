import random
import my_module

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

choose = int(input("What do you choose? 0:Rock, 1:Paper, 2:Scissors: "))


com_rand = random.randint(0,2)

if((choose==0 and com_rand==2) or (choose==1 and com_rand==0) or choose==3 and com_rand==2):
  print("You win")
elif(choose == com_rand):
  print("Save")
else:
  print("You loose")

print("You:")
if(choose==0):
  print(rock)
elif(choose==1):
  print(paper)
else:
  print(scissors)

print("Computer:")
if(com_rand==0):
  print(rock)
elif(com_rand==1):
  print(paper)
else:
  print(scissors)

