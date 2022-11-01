# a = [1,2,34,4,4,4,4]
# a[1]=1
# print(a)
# a.append(123)
# print(a)
# a.extend([1,2,3,4,5,6,7,8,9,1,22])
# print()
import random
a = (input('Enter the names of the person separated by a coma')).lower()
list_a = a.split(',')
print(a)
print(f"{random.choice(list_a)} is paying the bill today")
print(len(list_a))

