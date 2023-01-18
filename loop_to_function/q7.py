# Print the following pattern using function....
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

def pat(x):
    i = 1
    while x >= i:
        a = x
        while a >= i:
            print(a,end=" ")
            a-=1
        print()
        x-=1
    
nums = int(input("Enter any number :"))
pat(nums)