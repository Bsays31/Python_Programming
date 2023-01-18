# write a function to find the factorial of a given interger number.....?


def fac(x):
    mul = 1
    while x != 0:
        mul = mul * x
        
        x-=1
    print(mul)


nums = int(input("Enter any number to find its factorial :"))
fac(nums)