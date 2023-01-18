# Display numbers from a list using loop:
# Write a program to display only those numbers from a list that satisfy the following conditions....:
# *The number must be divisible by five 
# *If the number is greater than 150,then skip it and move to the next number 
# *If the number is greater than 500,than stop the loop

def itterate(x):
    list = []
    i = 1
    while i<= x:
        a = int(input("Enter the number that you want to append in the list :"))
        if a < 150 and a % 5 == 0:
            list.append(a)
        elif a > 500:
            break
        
        i+=1
    return list

nums = int(input("Enter the number of items you want in the list :"))
a = itterate(nums)
print(a)