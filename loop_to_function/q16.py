# Write a function the find the sum of the series upto n term.......?


def series(x):
    i = 0
    sum = 0
    while i < x:
        y = 0
        z = 0
        while y <= i:
            z = z * 10 + 2
            y+=1
        sum = sum + z
        i+=1
    return sum 

nums = int(input("Enter the number of terms :"))
a = series(nums)
print("After adding all the terms the sum total is :",a)