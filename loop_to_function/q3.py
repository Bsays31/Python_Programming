# Calculate the sum of all numbers from 1 to a given number....?

def sumall(x):
    sum = 0
    while x != 0:
        sum = sum + x
        x-=1
    return sum

nums = int(input("Enter any number :"))
a = sumall(nums)

print("The sum of all the numbers is",a)