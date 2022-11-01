print("Welcome to the love calculator")
name1 = input("enter your name? \n")
name2 = input("enter your name? \n")
name1 =  name1.upper()
name2 = name2.upper()
count = 0
count_ = 0
for i in name1+name2:
    if i in ['T','R','U','E']:
        count+=1
    if i in ['L','O','V','E']:
        count_+=1
print(f"Your love score is {count}{count_}")
"""the other way of doing it is ussing string.count()"""
print(f"for name there are {name1.count('L' or 'O')} no of l")