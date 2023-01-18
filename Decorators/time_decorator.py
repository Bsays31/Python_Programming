import time
#Creating a time decorator that calculates the time of the function execution...

def timer(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        z = f(*args,**kwargs)
        total = time.time() - start
        print("Total time = ",total)
        return z
    return wrapper

@timer
def func2():
    for _ in range(1000000):
        pass

@timer
def func3(x,y):
    return x+y

func2()
print(func3(55,1))