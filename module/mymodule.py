def greetings():
    print("Hello world!")

def add(a,b):
    return a+b

person1 = {
    "Name" : "Bishesh",
    "Age" : 22,
    "sex" : "Male"
}

def multi(a,b):
    return a*b


def pattern(x):
    i = 0
    while i < x:
        a = 0
        while a <= i:
            print("*",end=" ")
            a+=1
        print()
        i+=1


def prime(x):
    i = 2
    while i < x :
        if x%i==0:
            print("Not a prime number")
            break
        i+=1

    if i == x:
        print("It is a prime number")


def subtract(a,b):
    return a-b

def fibonicca(x):
    ft = 0
    st = 1
    i = 0
    while i < x :
        print(ft)
        nt = ft + st
        ft = st
        st = nt
        i+=1

