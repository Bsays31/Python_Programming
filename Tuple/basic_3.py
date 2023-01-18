# Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or
# indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous 
# and are accessed by iterating over the list.

# Note: In unpacking of tuple number of variables on the left-hand side should be equal to a number of values in given tuple a. 


# Accessing Tuple
# with Indexing
#Tuple1 = tuple("Geeks")
#print("\nFirst element of Tuple: ")
#print(Tuple1[0])


# Tuple unpacking
#Tuple1 = ("Geeks", "For", "Geeks")

# This line unpack
# values of Tuple1
#a, b, c = Tuple1
#print("\nValues after unpacking: ")
#print(a)
#print(b)
#print(c)



print("\nUnpacking tuple :")
t = ("Apple","Banana","Mango")

print("\nThis line will unpack the values of tuple :")
a,b,c = t

print(a)
print(b)
print(c)

b = ("Geeks")
print(b[0])