def rev (x):
    return helper(x,0)
    

    

def helper(x ,ans):
    if x == 0:
        return ans 

    rem = x % 10
    ans = ans * 10 + rem
    return helper(x//10,ans)

    


a1 = rev(6786)
print(a1)