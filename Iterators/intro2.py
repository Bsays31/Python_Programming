import sys
# Iterable object list...
a = [1,2,3,4,5,6,7,8,9,10]

# Using map function to iterate over iterable items...
# Map returns an iterator, thats means the actual values are nit generated we only generate this values when we are lopping 
# through it, it were not generated and stored in a memory, like when we "for i in y:" in first iteration it sends the value 1
# and gives the result and so on..... 
b = map(lambda i : i ** 2, a )
print("It will now return the iterator itself...")
print(b)

#using next() or b.__next__()
print(next(b))
print(b.__next__())

# Using a for loop to iterate..
# When we use a for loop to traverse any iterable object,internally it uses the iter() method to get an iterator object, which 
# further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.
for c in b:
    print(c,end=" ")
print()

# The whole point is we dont have to store the sequence in the memory we can generatev the sequence when we loop through it.. 
print(sys.getsizeof(a))
print(sys.getsizeof(b))
