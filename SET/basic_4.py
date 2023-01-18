# Using remove() method or discard() method:
# Elements can be removed from the Set by using the built-in remove() function but a KeyError arises if the element doesn’t
#  exist in the set. To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set,
#  it remains unchanged.

# Initializing a set....
set1 = set([1,2,3,4,5,6,7,8,7,8,90,9,10])
print("\nInitial set :")
print(set1)

# Removing an element form the set...
set1.remove(2)
set1.remove(3)
set1.remove(4)
print("\nSet after the removal of 3 objects :")
print(set1)

# Using discard() method 
set1.discard(90)
set1.discard(1)
print("\nSet after the discard of two objects :")
print(set1)

#Using range function in a loop to discard certain range of objects from the set....
for i in range(5,8):
    set1.remove(i)

print("\nSet after using the loop to remove certian range of objects :")
print(set1)

print()