def sum(x):
     return x+5


#A lambda function is a small anonymous function a lambda function can take any number of arguments, but can only have one expression.
#Syntax for lambda = lambda variable : expression
a1 = lambda x : x + 5
print(a1(5))




#map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.
#syntax : map (function,iterable_variable)
a = [1,2,3,4,5]
ab = list(map(sum,a))
print(ab)




#Map function with lambda function..
#Syntax : map(lambda variable : expression,iterable variable)
b = list(map(lambda x : x * 2,a))
print(b)

