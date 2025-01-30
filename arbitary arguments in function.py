# def greet5(*name):
#     # for n in name:
#     #     print("hello"+" "+n)
#     print(name)
# greet5("a","e","t","uu","bbb","hhhh")#fn call
#
# def greet6(greet,*name):
#     for n in name:
#         print(greet+" "+n)
#     #print(name)
# greet6("Hello","e","t","uu","bbb","hhhh")#fn call


#list comprehension
# n=[1,2,3,4,5]
#
# num=[]
# print(num)
# for i in n:#i=1,2,3,4,5
#     j=i*i
#     num.append(j)
# print(num)
# #
# numbers=[i*i for i in n]
# print(numbers)
n=[1,2,3,4,5]
num=[]
num=[i if i%2 != 0 else   for i in n]  #i=1,2,3,4,5
print(num)

