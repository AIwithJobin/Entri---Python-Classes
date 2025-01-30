# c = 0
# while c <= 5:
#     if c == 2:
#         c=c+1
#         continue
#     if c == 4:
#         break
#
#     print(c)
#     c = c + 1

# for c in range(6):
#     if c==4:
#         break
#     if c==2:
#         continue
#     print(c)
#
# def square(x):
#     y=x**2
#     print(y)
#     return y
# result = square(4)
# square(4)
# print(f"The square of number is {result}.")


d=int("input the number till where the table is required")
def multiply(a,b):
    for i in range(1,20):
        print(f"{i}*{d}={i*d}")
multiply()
