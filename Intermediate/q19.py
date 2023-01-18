# Calculate the LCM(LEast common multiple)?


def lcm(x):
    i = 1
    table = []
    while i!= 11 :
        a = x * i
        table.append(a)
        i+=1
    return(table)

nums1 = int(input("Enter the number :"))
nums2 = int(input("Enter the number :"))

a = lcm(nums1)
b = lcm(nums2)


set = (set(a) & set(b))
b = ()
for i in set:
    if i < b :
        b = set

