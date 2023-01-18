def Linear_Search(a , target):
   return  helper(a,target,0)




def helper(a,target,index):
    
    if index == len(a):
        return False

    if a[index] == target:
        return True

  

    
    return helper(a,target,index+1)






a = [0,1,2,3,3,4]
target = 4

ans = Linear_Search(a,target)
print(ans)