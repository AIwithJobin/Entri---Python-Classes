# print("hello")
# # print is a built in function
# print("test")
# print(10)
# b=20.5
# c=20.5
#
# print(id(b))
# print(id(c))

x={"jobin":2100,
   "rohith":1500,
    "nihal":2400,
    "name":2600,
   }
sum=0
for v in x.values():
    sum=sum+v

avg=sum/len(x)
for k in x.keys():
    x[k] =x[k]- avg
print(x)

# x={"name":["jobin","rohith","nihal","jerrit"],"spend":[2100,1500,2400,2600]}
# print(len(x))

# print(x{name})
#
# sum=0
# def average(x):
#     for spend in x
#         sum=sum+spend
#
#
#     if(x%2==0):
#          value="even"
#     else:
#          value="odd"
#     return value
# result=oddoreven(9)
# print("=",result)

# amountpaid=[2100,1500,2400]
# total=sum(amountpaid)
# correctsplit=total/float(len(amountpaid))
# split=[amount - correctsplit for amount in amountpaid]
# print(split)
#
# for amt in split:
#     if(amt==0):
#         print("pay 0 ")
#     elif(amt<0):
#         print("pay",amt)
#     else:
#         print("recieve",amt)
