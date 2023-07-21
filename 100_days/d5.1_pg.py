#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



password=''
for i in range(0,nr_letters):
  r_letter=random.randint(0,len(letters)-1)
  password=password+(letters[r_letter])
for j in range(0,nr_symbols):
  r_symbol=random.randint(0,len(symbols)-1)
  password=password+(symbols[r_symbol])
for k in range(0,nr_numbers):
  r_number=random.randint(0,len(numbers)-1)
  password=password+(numbers[r_number])
print(password)

n_password=''
characters=[letters,numbers,symbols]
list=[0]*nr_letters+[2]*nr_symbols+[1]*nr_numbers
print(list)
l_list=random.sample(list,len(list))
print(l_list)
r_list=sorted(list, key=lambda x:random.random())
print(r_list)
for i in l_list:
  if i==0:
    r_letter=random.randint(0,len(letters)-1)
    n_password=n_password+characters[i][r_letter]
  elif i==2:
    r_symbol=random.randint(0,len(symbols)-1)
    n_password=n_password+characters[i][r_symbol]
  elif i==1:
    r_number=random.randint(0,len(numbers)-1)
    n_password=n_password+characters[i][r_number]


print(n_password)