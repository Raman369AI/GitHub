print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1+name2
t_count=0
l_count=0
for a in name:
    if 'T'==a or 't'==a:
        t_count+=1
    if 'R'==a or 'r'==a:
        t_count+=1
    if 'U'==a or 'u'==a:
        t_count+=1
    if 'E'==a or 'e'==a:
        t_count+=1
   
for b in name:
    if 'L'==b or 'l'==b:
        l_count+=1
    if 'O'==b or 'o'==b:
        l_count+=1
    if 'V'==b or 'v'==b:
        l_count+=1
    if 'E'==b or 'e'==b:
        l_count+=1

s_count=str(t_count)+str(l_count)
if int(s_count)>90 or int(s_count)<10:
    print(f'Your score is {s_count}, you go together like coke and mentos.')
elif int(s_count)<50 and int(s_count)>40:
    print(f'Your score is {s_count}, you are alright together.')
else:
    print(f'Your score is {s_count}.')