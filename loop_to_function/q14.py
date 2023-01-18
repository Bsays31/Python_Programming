# write a function to use a loop to display elements from a given list present at the odd index position....?

def odd(x):
    i = 0
    j = 2
    while i < len(x):
        if i % j != 0:
            print(x[i])
        i+=1



nums = [10,20,30,40,50,60,70,80,90,100]
odd(nums)