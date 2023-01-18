n = int(input("Enter the total :"))
r = int(input("Enter how many times you want :"))

f1 = 1
for i in range(1,n+1):
    f1=f1*i

f2 = 1
for i in range(1,r+1):
    f1 = f1*i

f3 = 1
for i in range(1,(n-r)+1):
    f3 = f3 * i

ncr = f1 / (f2 * f3)
npr = f1 / f3

print("Ncr is",ncr)
print("Npr is",npr)
