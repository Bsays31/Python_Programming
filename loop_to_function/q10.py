# Write a program to display all prime numbers within a range....?
# start = 25, End = 50


def rangeprime(x,y):
    for i in range(x,y):
        a = 2
        while i > a:
            if i % a == 0:
                break
            a+=1
        if i == a:
            print(i)

start = 25
end = 50
rangeprime(start,end)