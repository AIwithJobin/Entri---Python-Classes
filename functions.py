#built -in functions
# l1=[1,2,3,4,5]
# print(sum(l1))

# abs()
# Example: abs(-1.5)
# print(abs(-1.5))
# round()
# Example: round(3.5678, 2)
# print(round(3.5678,2))
# len()
# Example: len("Python")
# max()
# Example: max(4, 7, 2)
# min()
# Example: min(8, 5, 9)
# sum()
# Example: sum([1, 2, 3, 4])
# sorted()
# Example: sorted([3, 1, 2])
# type()
# Example: type(3.14)
# str()
# Example: str(123)
# int()
# Example: int(4.6)
# float()
# Example: float(3)
# pow()
# Example: pow(2, 3)
# print(pow(2,3))#=2*2*2
# input()
# Example:
# name = input("Enter your name: ")
# print(name)
# range()
# Example: list(range(3))
# print()
# Example: print("Hello, World!")
# bool()
# Example: bool(0)
# list()
# Example: list((1, 2, 3))
# tuple()
# Example: tuple([4, 5, 6])
# isinstance()
# Example: isinstance(5, int)
# help()
# Example: help(print)"""

#user defined functions
#
#syntax
# def fn_name(arguments/variables/parameters):
# block of code
# function_call

# def sum_1(x,y):
#     z=x+y
#     print("sum",z)
#     return z
# sum_1(2,3)
#
# print("Heloo")
# result=sum_1(10,20)
# print("Sum=",result)
#
#
# def product(x,y):
#     z=x*y
#     return z
# result=product(10,20)
# print("Product=",result)
#
# name=input("Enter your name:")
# def greet():
#     print("Hello",name)
# print("Hi")
# print(6+7)
# greet()
#
# def oddoreven(x):
#     if(x%2==0):
#          value="even"
#     else:
#          value="odd"
#     return value
# result=oddoreven(9)
# print("=",result)


#local and global variables or namespace
balance=1000 #global variable
mp=100
def display():
    balance=2000 #local variable
    balance+=2000 #balance=balance+2000
    print(balance)
    print(mp)
    global local1
    local1=10
    print(local1)
    global local2
    local2=13
    print(local2)
display()#fn call
print(balance)
print(mp)
print(local1)
print(local2)

