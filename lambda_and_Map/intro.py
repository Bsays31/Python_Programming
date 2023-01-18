# def fun(x):
    
#     return x+5

# print(fun(3))

# fun1 = lambda x : x+5
# print(fun1(4))

def fun3(x):
    fun1 = lambda x : x+5
    return fun1(x)


print(fun3(5))