#lambda functions
#they are functions used to create small functions that does not have  many lines can be done in a single line

#lambda function
#anonymus function
#syntax
# variable_name = lambda(variable/arguments:expression)


# def square_of_num(x):
#     x=x**2
#     return x
# result=square_of_num(4)
# print(result)
#
# square = lambda x:x**2
# print(square(3))

# sum_fn =lambda x,y,z:x+y+z
# print(sum_fn(3,4,9))
#
# x=int(input("Enter the integer"))
# check= lambda x: "even" if x%2==0 else "odd"
# print(check(x))

#Some special fns
#Recursion
#calling same fn within that fn
#factorial of a number
# def fact(x): #factorial of 3
#     if(x==1) or (x==0):
#         return 1
#     else:
#         return (x*fact(x-1)) #3*fact(2)=3*2*fact(1)=3*2*1
# result=fact(3)
# print(result)