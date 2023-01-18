# Dictionary in Python is a collection of keys values, 
# used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# Creating a dictionary :
dict1 = {"Name1" : "Bishesh",
"Name": "Niten"}
print("\nDictionary :")
print(dict1)

# In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
#  Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value.
#  Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

# Note – Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 

# Creating a dictionary with integer keys :
dict1 = { 1 : "Bishesh Gurung",
        2 : "Niten sapkota",
        3 : "Norbu sherpa",
        4 : "Anmol prasad"}
print("\nDictionary with the interger keys :")
print(dict1)

# Creating a doctionary with mixed keys :
dict1 = {"Name" : "Bishesh",
        1 : [1,2,3,4]}
print("\nDictionary with the use of mixed keys :")
print(dict1)

#Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}. 

# Creating an empty dictionary..
dict1 = {}
print("\nEmpty dictionary :")
print(dict1)

# Creating a dictionary with the use of dict() method..
dict1 = dict({1 : "Bishesh",2 : "niten"})
print("\nCreating a dictionary wiht the help of dict() method :")
print(dict1)

dict1 = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(dict1)

# Creating a nested dictionary.....
dict1 = {1 : "Bishesh",2 : {"Niten","norbu","anmol"}}
print("\nCreating a nested dictionary :")
print(dict1)

print()