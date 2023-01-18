# In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
# The order of elements in a set is undefined though it may consist of various elements. The major advantage of using a set,
# as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.

#Python program to demonstrate creation of Set :


#Creating a set :
set1 = set()
print("\nInitializing a blank set :")
print(set1)

#creating a set with the use of strings:
set1 = set("GeeksForGeeks")
print("\nSet with the use of strings :")
print(set1)

#Creating a set with the use of constructor (using objects to store strings)
set1 = "GeeksForGeeks"
set2 = set(set1)
print("\nSet with the use of an object :")
print(set2)

#Creating a set with the use of list :
set1 = set(["Geeks","For","Geeks"])
print("\nSet with the use of list :")
print(set1)

#Creating a set with the use of mixed values:
set1 = set([1,2,"Geeks",4,5,5,"For",66,77,88,88,"Geeks"])
print("\nSet with the use of mixed values :")
print(set1)

#Another Method to create sets in Python3
# Set containing numbers
my_set = {1, 2, 3}
print("\nSet that has already been defined :")
print(my_set)