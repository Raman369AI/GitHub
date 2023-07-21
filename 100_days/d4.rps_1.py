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
options=[rock,paper,scissors ]

while True:
  userchoice=int(input('enter your choice among rock,paper,scissors '))
  if (userchoice in range(0,3)):
    break

print(f"userchoice is {options[userchoice]}")
computerchoice=random.randint(0,2)
print(f"computerchoice is {options[computerchoice]}")

if userchoice==computerchoice:
  print('Its a draw!')
elif userchoice==0 and computerchoice==1:
  print('you loose')
elif userchoice==2 and computerchoice==0:
  print('you loose')
elif userchoice==1 and computerchoice==2:
  print('you loose')
else:
  print('You win')