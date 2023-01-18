import csv

def thanks(f):
    def wrapper(*args,**kwargs):
        print("Your amount is :",end=" ")
        z = f(*args,**kwargs)
        print("Thank you for purchasing from our website...")
        return z
    return wrapper

@thanks
def addition(x,y):
    print(x+y)


addition(22,3)