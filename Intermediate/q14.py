# Calculate armstrong number.....?

nums2 = nums = nums1 = int(input("Enter any number to calculate its armstrong number :"))
count = 0

while nums2 != 0:
    count = count + 1
    nums2//=10

sum = 0 


while nums != 0:
    a = nums % 10
    power = pow(a,count)
    sum = power + sum
    nums //= 10

if nums1 == sum :
    print("It is an armstrong number.")
else :
    print("Not an armstrong number.")