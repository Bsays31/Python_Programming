def greeting():
    print("Hello motherfucker! ")

def primenumber(x):
    i = 2
    while i < x:
        if x % i == 0:
            print("Not a prime number")
            break
        i+=1
    if i == x:
        print("Prime number")

