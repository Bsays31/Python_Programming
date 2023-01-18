num = 23
print("Type of num is:", type(num))

lst = [1, 2, 4]
print("Type of lst is:", type(lst))

name = "Atul"
print("Type of name is:", type(name))



# Every type in Python is defined by Class. So in the above example, unlike C++ or Java where int, char, float are primary
#  data types, in Python they are objects of int class or str class. So we can make a new type by creating a class of that type.
#  For example, we can create a new type of Student by creating a Student class. 


class Student:
	pass
stu_obj = Student()

# Print type of object of Student class
print("Type of stu_obj is:", type(stu_obj))


# A Class is also an object, and just like any other object, it’s an instance of something called Metaclass. A special class
# type creates these Class objects. The type class is default metaclass which is responsible for making classes.
# In the above example, if we try to find out the type of Student class, it comes out to be a type. 