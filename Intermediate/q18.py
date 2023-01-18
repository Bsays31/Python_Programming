# Make a program to calculate the HCF of two numbers ?

def hcf(x):
    list=[]
    i = 0
    mul = 2
    y = 0
    while x > y :
        while x > 0:
            while x % mul == 0:            
                z = x // mul
                list.append(mul)
                x = z
            break
                
        mul+=1
        y+=1
    list.append(1)
    return(list)




a = int(input("Enter any number to find its HCF :"))
b = int(input("Enter the number to find its HCF :"))

if b > a:
    mn = b

else:
    mn = a



for i in range(1,mn+1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("The HCF of these two numbers is",hcf)