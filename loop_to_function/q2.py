# Print the following pattern...
#write a program to print the following pattern using a while loop...
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5

def pattern(x):
    i = 0 
    while x >= i:
        a = 1
        while a <= i:
            print(a,end=" ")
            a+=1
        print()
        i+=1


nums = int(input("Enter the number to print the pattern :"))
pattern(nums)