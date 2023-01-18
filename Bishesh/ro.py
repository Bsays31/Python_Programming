nums = int(input("Enter any number :"))
i = 1

while i <= nums :
    a = 1
    while a <= i:
        print(a,end=" ")
        a+=1
    print()
    i+=1
j = 1

while j <= nums:
    y = nums 
    while y < j:
        print('*',end="")
        y-=1
    print()
    j+=1