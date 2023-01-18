# Write a function that prints the multiplication table of a given number...?



def multiplication(x):
    i = 1
    while i <= 10:
        mul = x * i
        print(mul)
        i+=1
    

nums = int(input('Enter any number :'))
multiplication(nums)

