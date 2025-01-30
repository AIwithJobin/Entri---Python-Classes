
t1=(1,2,3,4,5)
t2=1,2,3
t0="hi","a"
t3=("hello","hi")
t4="hello","hi"
# print(t3)
# print(t4)
# print(id(t3))
# print(id(t4))
t5=t3,t1
# t6=t2,t4
# t7=(t1,t4)
# print(t5)
# print(len(t5))
# print(t5[1])
# print(t5[1][1])
# print(t5[0][1])
# print(t6)
# print(t7)



# # #
l1=[1,2,3]#list
s=set(l1)
t=tuple(l1)
print(s)
print(t)
# print(t[2])

t10='hi'
print(type(t10))
t11=('hi',)
print(type(t11))
test=('hi','hello')
print(type(test))
t12='hi'*3
print(t12)
t13=('hi')*3
print(t13)
print(type(t13))
# #
test2=('hi','hello')*3
print(test2)#interview point
print(type(test2))


tuple_new=(1,"hello",1,2.5,(1,2,3,4),[10,11,12])
print(tuple_new,len(tuple_new))



#accessing
indext1=(1,2,3,4,5,6,7,8,8,"hi")
print(indext1)
print(indext1[3])
# # #slicing
print(indext1[1:6])
#
# # #unpacking method (interview point)
tupleNew=(1,5,7)
a,b,c=tupleNew
print(a,b,c)
# # print(tupleNew)
# print(len(tupleNew))
#
# a,b,c=10,"hi",7.5
# print(a,b,c)
# a=
#
# a=b=c=
#
# e=f=g=100
# print(e,f,g)
# #
listnew=list(tupleNew)
print(id(tupleNew))
listnew[1]=10
print(listnew)
# listnew.pop(2)
# listnew.append(8)
# tupleNew=tuple(listnew)
# print(tupleNew)
