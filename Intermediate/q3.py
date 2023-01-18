# Calculate the average of n number ?

nums = int(input("Enter a number :"))

sum = 0

i  = 0

while nums > i:
    nums1 = int(input("Enter the number to calculate the average :"))
    sum = sum + nums1
    i+=1

average = sum // i
print(average)
