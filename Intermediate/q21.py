# What is a perfect number ?

nums1  = nums = int(input("Enter a number to check if is a perfect number or not :"))

sum = 0

i = 0

while nums > i:
    a = 1
    if nums % a == 0:
        sum = sum +a
    a+=1
    i+=1

if sum == nums1:
    print("It is a perfect number.")
else :
    print("not a perfect number.")
