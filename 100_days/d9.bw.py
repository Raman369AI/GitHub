import os
import operator

def bid():
    person={}
    name=input('Enter your name\n')
    person[name]=input('Enter your amount\n')
    direction=input('Do you want to continue? yes, no\n').lower()
    if direction=='yes':
      os.system('clear')
      bid()
    else:
      os.system('clear')
      sorted(person.items(),key=operator.itemgetter(1))
      print(f"{person.popitem()} is the winner")


bid()