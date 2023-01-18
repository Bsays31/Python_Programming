# A Generator function is defined like a normal function but whenever it needs to generate a value, It does so with the 
#"yield" keyword rather than return, if the body of the function contains a 'yield' keyword it automaticlly becomes a generator..

def generators(x):
    for i in x:
        yield i * 2



a = [1,2,3,4,5,6]
for a in generators(a):
    print(a,end=" ")


# Generator-Object : Generator functions return a generator object. Generator objects are used either by calling the next method 
# on the generator object or using the generator object in a “for in” loop (as shown in the above program). 
