


print("welcome to the pizza shop")
size = input("what size if the pizza do you want? S M or L")
size = size.upper()
extra_C = input("would you like some extra cheese? Y N ")
extra_C = extra_C.upper()
add_p = input("Do you want ppeporoni? Y or N ")
add_p = add_p.upper()

bill = 0
if size == "L":
    bill = bill+25
    if add_p == "Y":
        bill+=3
elif size == "M":
    bill = bill+20
    if add_p == "Y":
        bill+=3
elif size == "S":
    bill += 15
    if add_p == "Y":
        bill+=2
else:
    print("invalid input")
if extra_C == "Y":
    bill+=1

print("total bill is : ",bill)
