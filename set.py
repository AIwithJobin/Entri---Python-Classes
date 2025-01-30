#set

#mutable and unordered
#duplicates are not allowed
#set and dictionary are also defined with {}



#creation
# s1=set()#if we want to create a null set use the set function or else it will become a dictionary
# print(s1,type(s1))
#
# s0={}#dictionary
# print(s0)
# print(type(s0))

# s101={1,2}
# print(type(s101))

l1=[8,1,3,5,7,7,"hi"]
print(l1)
s2=set(l1)#type conversion
print(s2)
print(s2)
# print(s2[1])#indexing not possible

s3={1,2,3,3,4,5}
print(s3)
#adding elements
s3.add(7)
print(s3)
#
# #removing elements
s3.remove(4)
print(s3)


# joining operations

# #and/intersection
# s3={1,2,3,3,4,5}
# l1=[8,1,3,5,7,7,"hi"]
# s2=set(l1)
# print(s2,s3)
#
# # print(s2&s3)#and intersection
# # s4=s2&s3
# # print(s4)
# # #
# # print(s2-s3)#difference
# print("Difference s3-s2",s3-s2)
# print("Common elements",s3&s2)
# #
# print(s3|s2)#or/union
# print(s2|s3)
