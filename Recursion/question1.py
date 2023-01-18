# write a program to take a user input from the user and print the number from 1 to the given number using recursion ?

def number(x):
    return helper(x,0)

def helper(x,y):
    if x == 0:
        return

    y = y + 1
    print(y)
    helper(x-1,y)

a = int(input("Enter any number ="))
number(a)