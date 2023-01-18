# Using pop() method:
# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set. 

# Initial set...
set1 = set([1,2,3,4,5,6,7,8,9])
print("\nInitial set :")
print(set1)

# Using pop() method..... 
set1.pop()
print("\nSet after popping the elements :")
print(set1)

# Using clear() method:
# To remove all the elements from the set, clear() function is used. 

set1.clear()
print("\nSet after using the clear() method :")
print(set1)

# Frozen sets in Python are immutable objects that only support methods and operators that produce a result without 
# affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time, 
# elements of the frozen set remain the same after creation. 

# If no parameters are passed, it returns an empty frozenset.  

# Python program to demonstrate
# working of a FrozenSet
 
# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
 
Fset1 = frozenset(String)
print("\nThe FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())
