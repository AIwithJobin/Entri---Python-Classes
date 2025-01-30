#
# #diff data types
# x=10
# y=2.5
# z="Hello"
# # a=False
# # print(type(x),type(y),type(z),type(a))
# #
# # # data structures are onects which can store or carry multiple elements
#
# #list data structures
# numbers=[11,22,13,234,35,46]
# print(numbers)
# print(type(numbers))
# print(numbers[1:4])
#
# #there are two types of data
# #print(structures..)user defined and built in data structures
#
# # built in data structures
# # list,tuple,set,dictionary,string
# #string is a data type and a data structure

# y=2.5

# string Data structues

# z="Hello welcome "
# # print(y[1]) # element accessing
# print(z[1:12]) # element slicing
# print(z[1:12:2])
# print(z[1:12:3])
# #start end step
# print(z[::-1])
# word = "english"
# print(word[-1])
# print(word[::-1])

# data structure properties
#1.order # having index number or not
#2.mutability #
# print(id(word))
# word= word+"c"
# print(id(word))
# word= word+"X"
# print(id(word))

# l1=[1,2,3]
# print(id(l1))
# l1[2]=10
# print(id(l1))
# # print(l1)
# Robot=""" Hi I'm a "Robot" """
# print("Hi I\'m a \"Robot\" ")
#
# print(Robot)

# list data structuress
#list is mutable and ordered ,mixed data type is possible(heterogeneous)

#List
# #mutable,ordered,mixed data type elements (heterogeneous) ,allows duplicate values
#[]

#
age=[35,38,'a',True,38]
# print(age)
# print(id(age))
# age.append("Hi")
# print(age)
# print(id(age))
# print(age[2])
# print(age[1],age[-2])
# Age=[1,4,7]
# #null list#check variable name and case senitivity
# print(Age,type(Age))
#
# print(age,Age)
# print(len(age))#len for counting elements in a list
# l1=[]
# print(l1)
# AGE =list()
# print(AGE)
# l1=list("jobin")
# print(l1)
# #The quick brown fox jumps over the lazy dog
# A=list("The quick brown fox jumps over the lazy dog.")
# print(len(A))
# l2=["jobin","melani"]
# print(l2)
# num=[1,2,3,4,5]
# print(num)
# c=list(range(1,10010))
# print(c)
# d=list(range(2,51,3))
a1=[1,2,3,]
a2=[4,5,6]
a3=a1+a2
print(a3)


# print(d)
#
# adding new elements
age.append(1000)
print(age)
age.extend([2000,3000,4000,5000])
print(age)

age.extend(list(range(1,10)))
print(age)

age.insert(1,"welcome")
print(age)


#pop
age.pop(-1)
print(age)
#remove
age.remove(38)
print(age)
#delete
del age[4]
print(age)
# del age
# print(age)
#

#sorting
randomnum=[45,89,13,34,1,89,3]
randomnum.sort()
print(randomnum)
#
# randomnum.reverse()
# print(randomnum)
randomnum=randomnum[::-1]
print(randomnum)
#
#tuple
#ordered
#immutable
#created using ()and comma ,  separated
a="hello","hi",1
print(a)
print(type(a))