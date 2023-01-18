#It is a quick way to change the functionality of the function without changing the code....
#Creating a decorator without returning the function 

def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        
        #calling the func function..
        f(*args,**kwargs)
        print("Ended")

    #The func function will return the wrapper function as an object
    return wrapper

@func
def func2(x,y):
    print(x+y)


@func
def func3(x,y):
    print("I am func3")


func2(4,5)
