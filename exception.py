#also some anonynoums exceptions
# try:
#     num = int(input("Enter a number > 0:"))
#     if num<=0:
#         raise Exception
#     else:
#         print(num)
# except Exception:
#     print("Enter a valid number")

# num=int(input("Enter an even number"))
# try:
#     if num%2!=0:
#         print("hi")
#         raise Exception
#     else:
#         print("Square of number is", num**2)
# except Exception:
#     print("Enter a even number")

# #
b="hi"
c=int(b)
print(c)

a=input("the string which is to be converted to int")
try:
    b=int(a)
    print(b,"the string converted to integer")
# except ValueError:
#     print("This string cannot be converted to integer")

except Exception as e:
    print("This string cannot be converted to integer:",e)