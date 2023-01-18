# Using add() method
# Elements can be added to the Set by using the built-in add() function. Only one element 
# at a time can be added to the set by using add() method, loops are used to add multiple elements at a time 
# with the use of add() method.

#Initializing a blank set:
set1 = set()
print("\nInitializing a blank set:")
print(set1)


#Using add method to add new elements to the set :
set1.add(4)
set1.add(9)
set1.add((6,7))
print("\nUsing add method to add new elements to the set :")
print(set1)


#Using loop to add alements to the set:
for i in range(1,9):
    set1.add(i)
print("\nUsing loop to add alements to the set:")
print(set1)


# Using update() method
# For the addition of two or more elements Update() method is used. The update() method accepts lists,
# strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

set1 = {1,2,3,(4,5),"BG",3,4,5,"BG"}
set1.update([7,8,9])
print("\nWe can also use this update()method to add new elements to the set :")
print(set1)