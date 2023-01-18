# Using build in methods and builet in functions:

t = (11,22,3,4,5,5,5,6,7,8,9,9,9)

#Build-in method....
print("\nBuild-in method to count the number of same items in a tuple :")
print(t.count(9))

print("\nBuild-in method to find the index of the specific element :")
print(t.index(7))

#Build-in function....
print("\nBuild-in function to return true if the elements are true or the tuple is empty :")
a = all(t)
print(a)

print("\nBuld-in function to return true if the tuple is true and false if the tuple is empty :")
a1 = any(t)
print(a1)

print("\nBuild-in function to return the maximun element of a given tuple :")
b = max(t)
print(b)

print("\nBuild-in function to print the minimum element of a given tuple :")
b1 = min(t)
print(b1)

print('\nBuild-in function to sum up the numbers of element of a given tuple :')
print(sum(t))

print("\nBuild-in function to input element in the tuple and return a new sorted list :")
c = sorted(t)
print(c)


print()