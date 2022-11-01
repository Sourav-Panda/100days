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



b = ['rock','paper','scissors']
dict_ = {'rock':rock,'paper':paper,'scissors':scissors}
b = random.choice(b)
a = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
try:
    if a ==0:
        print("you choosed rock", dict_['rock'])
        if b == 'rock':
            print(f'computer chossed {b}\n', dict_[b] )
            print("DRAW......")
        elif b =='paper':
            print(f'computer chossed {b}\n', dict_[b] )
            print("won......")
        else:
            print(f'computer chossed {b}\n', dict_[b] )
            print("lost......")

    if a ==1:
        print("you choosed paper", dict_['paper'])
        if b == 'rock':
            print(f'computer chossed {b} \n', dict_[b] )
            print("won......")
        elif b =='paper':
            print(f'computer chossed {b}\n', dict_[b] )
            print("draw......")
        else:
            print(f'computer chossed {b}\n', dict_[b] )
            print("lost......")
    if a ==2:
        print("you choosed scissors", dict_['scissors'])
        if b == 'rock':
            print(f'computer chossed {b}\n', dict_[b] )
            print("LOST......")
        elif b =='paper':
            print(f'computer chossed {b}\n', dict_[b] )
            print("won......")
        else:
            print('computer chossed {b}\n', dict_[b] )
            print("DRAW......")
    else:
        print("invalid input you lost")
except e:
    print(e)
    print("invalid input")