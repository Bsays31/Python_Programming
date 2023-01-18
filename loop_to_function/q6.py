# Write a function to count the total number of digit in a given number...?


def co(x):
    cou = 0
    i = 0
    while i < x:
        a = x % 10
        cou = cou + 1
        x //= 10
    return cou

nums = int(input("Enter the number to count :"))
b = co(nums)
print("There are",b,"digits in the number.")