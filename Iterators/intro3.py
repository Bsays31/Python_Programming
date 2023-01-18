x = [1,2,3,4,5,6,7,8,9,10]
y = map(lambda i : i**2, x)


while True:
    try:
        
        print(next(y))
    except StopIteration:
        print("Index error")
        break