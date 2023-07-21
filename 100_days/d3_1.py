print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
if size=='S':
    bill=15
    if add_pepperoni=='Y' :
        bill=17
if size=='M':
    bill=20  
    if add_pepperoni=='Y':
        bill=23
if size=='L':
    bill=25
    if add_pepperoni=='Y' :
        bill=27

if extra_cheese=='Y':
    bill+=1

print(f'Your final bill is: ${bill}.')