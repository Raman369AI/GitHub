from random import randint
number=randint(1,100)
def level():
  l=input("What level do you choose").lower()
  if l=="easy":
    return 10
  else:
    return 5
turns=level()
while turns>0:
  user=int(input("Enter a number"))
  if user<number:
    turns=turns-1
    print("The no is low, one chance down")
  elif user>number:
    turns=turns-1
    print("The no is high, one chance down")
  elif user==number:
    print(f"Done {user} is the number")
    break
if(turns==0):
  print("You have run out of chances.")
else:
  print("Congrats you win")