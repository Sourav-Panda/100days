# randomisation and python list
import random
import module
#rock paper sisor game
# mersenne twister
print(random.randint(10,100))
print(module.pi)
print(f"the outcome of the toss is {random.choice(['Head','Tail'])}")
a = random.randint(0,1)
if a == 0:
    b = 'Head'
else:
    b = "Tail"
print(f"the outcome of the toss is {b}")