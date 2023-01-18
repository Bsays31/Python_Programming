# Print first 10 natural numbers using whilne loop....?

def firstnat(x):
    i = 0
    while x > i:
        print(i)
        i+=1


nums = int(input("Enter any number to print :"))
firstnat(nums)