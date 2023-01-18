#Iterators

#Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

#__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object


#__next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object,
# internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. 
# This method raises a StopIteration to signal the end of the iteration.

# The .__iter__() method..
a = "Bisheshgurung"
print(a.__iter__())

for i in a :
    print(i,end=" ")
print()


b = [1,2,3,4,5,6,7,8,9,10]
c = b.__iter__()
print(c)

#The next() or .__next() method..
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))