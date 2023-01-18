# Write a function to reveerse a given integer....?

def re(x):
    rev = 0
    
    while x != 0:
        a = x % 10
        rev = rev * 10 + a
        x //= 10
        
    return rev

b = int(input("Enter digits to reverse :"))
ans = re(b)
print(ans)