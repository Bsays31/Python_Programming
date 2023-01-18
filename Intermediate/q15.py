# Calculate NCR and NPR ?

n = int(input("Enter the value of n :"))
r = int(input("Enter the value of r :"))
#Calculateing the value of n!
i = 1
f1 = 1
while n >= i:
    f1 = f1 * i
    i+=1

#Calculating the value of r!
i = 1
f2 = 1
while r >= i:
    f2 = f2 * i 
    i+=1

#Calculating the value of (n - r)!
f3 = 1
i = 1
a = n - r
while a >= i:
    f3 = f3 * i
    i+=1


ncr = f1 / (f2 * f3)
npr = f1 / f3

print("The NCR is",ncr)
print("THe NPR is",npr)