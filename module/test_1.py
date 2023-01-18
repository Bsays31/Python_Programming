import mymodule as b
# In the upper condition we defined mymodule as b so it wont be time consuming anymore we can use anything in the place of b....

# For importing only one function or any variable defined by us from the module :
# from module import add
# a = add(1,2)

print("\nCalling the greeting function :")
b.greetings()

print("\nCalling the add function :")
a = b.add(4,5)
print(a)

print("\nCalling the key from the defined dictionary :")
print(b.person1["Name"])

print("\nCalling the multiplication function :")
c = b.multi(4,6)
print(c)


print("\nCalling the pattern function :")
b.pattern(5)





#There is a build_in function to list all the function names(or variable names) in a modulo. The "dir()"function...
import platform

print("\nCalling build_in function to list all the function names and variables from platform module :")
x = dir(b)
print(x)

print("\nThis function shows what system are you currently using:")
ab = platform.system()
print(ab)