# Write a function to calculate the cube of all numbers from 1 to a given number....?


def cube(x):
    i = 1
    power = 0
    while i <= x:
        power = pow(i,3)
        print("Current number :",i," and the cube is :",power)
        i+=1

nums = int(input("Enter the number to calculate its cube :"))
cube(nums)
    