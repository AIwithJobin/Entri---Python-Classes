# fn isnide a fn
a=1000
def outer_fn():
    b=34
    print("heloo")
    def inner_fn():
        v=10
        print("Inside fn",v,b,a)
    inner_fn()
    print("values",b,a)
print("Hi")
outer_fn()


# Different types of argumnets

#positional arguments
def greet(name,msg):
    print("hello"+" "+msg+" "+name)
greet("Manu","Gd eve")

# #default argument
def greet2(name,msg,age="21"): #try name="default", msg
    print("hello"+name+msg,age)
greet2("Tanu","run")
greet2("Tanu","Run",25)
# greet2("anu",msg="walk")
def greet2(name,msg="Run",age=23): #try name="default", msg
    print("hello"+name+msg,age)
greet2("Tanu","Walk",56)


#keyword arguments
#position of argument is not an issue
def greet3(name,msg):
    print("hello"+name+msg)
greet3("walk",msg="Mithul")


def greet3(name,msg,age):
    print("hello"+name+msg+age)
greet3("Mithul",age="25",msg="walk")