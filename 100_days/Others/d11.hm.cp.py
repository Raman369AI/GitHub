

import random
def add(l):
  a=0
  for i in l:
    a=a+i
    if i==11 and a>21:
        a=a-10
  return a
  

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
i=0
while i<2:
  user_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))
  i+=1

scores=[add(user_cards),add(computer_cards)]
if scores[0]==21:
        print("You win, got a black jack")
        
elif scores[1]==21:
        print("Computer win , got a black jack")
       
else:
        print(f"your score is {scores[0]} and 1st computer card is {computer_cards[0]}")
while True:
  if scores[0]==21 and scores[1]==21:
    break
  if scores[0]!=21 and scores[1]!=21:
     direction=input("Do you want to continue? Yes or No\n").lower()
     if direction=='yes':
        user_cards.append(random.choice(cards))
        print(f"user score is {add(user_cards)}")
        
        if add(user_cards)>21:
         print("Computer win as user score breached 21")
         break
        elif add(user_cards)==21:
           print("you win as score reached 21")
           break
        elif add(user_cards)<21:
            while (add(computer_cards)<=16):
               computer_cards.append(random.choice(cards))
            
     elif direction=='no' and add(user_cards)>add(computer_cards):
          print("You win as your score greater")
          print(computer_cards) 
          print(user_cards)
          break
     elif direction=='no' and add(user_cards)<add(computer_cards):
          print("Computer win")
          print(computer_cards) 
          print(user_cards)
          break
     else:
          print('draw')
          print(computer_cards) 
          print(user_cards)
          break
else:
  pass

    