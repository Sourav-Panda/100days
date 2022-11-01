#conditional statement, logical operators, code block, Scope
 #if/else
 #if condition:
#     do this
# else:
#     do this
#nested if else
#if condition 1:
    #do this
    #if condition 2:
        #do this
    #esle:
        #do this
#else:
    #do this

#comparasion operators
# == to check equalilty
# >/< to check greater than and less than
#!= cheks not equal to


#cooding exercise



# num = int(input("Enter a number: "))
# if num == 0:
#     print("invalid input")
# elif num%2 ==0:
#     print(f"{num} is divisible by 2 and is an even number")
# else:
#     print(f"{num} is not divisible 2 and a odd number" )

#nested if anf else
height = float(input("please input your height"))
weight = int(input("enter your weight"))
BMI = float(weight)/(float(height)**2)

print("your BMI is ",int(BMI))

if BMI <18.5:
    print("underweight")
elif BMI<25 and BMI>18.5:
    print("normal weight")
elif  BMI>25 and BMI<30:
    print("over weight")
elif BMI<35 and BMI > 30:
    print("obese")
elif BMI>35:
    print("clinically obese")