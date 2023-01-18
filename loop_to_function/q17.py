# Write a function the print the following pattern.....
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern(x):
    i = 0
    while i < x:
        a = 0
        while a <= i:
            print("*",end=" ")
            a+=1
        print()
        i+=1
    j = 0
    while j < x :
        z = 1
        while z < x:
            print("*",end=" ")
            z += 1
        print()
        x-=1

nums = int(input("Enter any number :"))
pattern(nums)