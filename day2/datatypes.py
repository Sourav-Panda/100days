#data types
#String


string_ex = 'this is a string'
print("Hello"[0]) #this is know as subscripting it takes the forst char of the string -1 prints the last.
print('123'+'456')
#Integer
#  (numbers with out decimal places)
print(123+456)
#instead of ussing comas you can use _ (underscore)
long_num = 1_00_000
print(long_num,type(long_num))
#Float
#   Decimal values
float_num = 1.22
print(float_num,type(float_num))
#Boolean
#This is True or False
t_bool = True #note the t is capital T in True
f_bool = False
#---------------------------------------------------
#Function takes input do process and retuns an output
#the input to the function can be of a fixed data type ex: len() takes string as input
#while doing string concatination we can concatinate only strings and not integers or floats
#it can be done int the following way
concat_string = str(long_num)+string_ex #str() is used to conver to string data type, int() for int and float() float
print(concat_string)
#not if you conver a float to int it will lose the decimal information
print(int(float_num))
# mathematical operators:
    # + addition
    # - substraction   
    # * multiplication
    # / division
    # ** power
    # //
#priority PEMDAS paranthesis exponent (mul division) addition substaction it slightly different to bodmas
#Round (round to the closest integer)
a=2.44444
b=2.66666
print(a,round(a))
print(type(5//4)) # // gives the hightest data type in the input i.e. if there are only int the output will be an integer
#f there is a float it will be a float
#result += 1  is equivalent to result = result+1
#=-------------------------------------------------------------------------------------------
#fstrings 
print(f"hello yout bmi is{a} which is obesecl")