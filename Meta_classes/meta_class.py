class Bsays(type):

    def __new__(cls,class_name,bases,attributes):
        #attributes before..
        print(attributes)

        a = {}

        for key,value in attributes.items():
            
            #Leaving all the keys starting with double underscore..
            if key.startswith("__"):
                a[key] = value


            #Converting all the keys to upper case 
            else:
                a[key.upper()] = value


        #attributes after ....
        print(a)
        return type(class_name,bases,a)

class Dog(metaclass=Bsays):
    x = 5
    y = 8

    def bark(self):
        print("Wooffff!!!")



#This block of code won't work because we've now modified our type constructor in our meta class
#as everything in the class except starting with "__" is comverted to upper case....
a = Dog()

print(a.X)
print("I am executed..")


#instead use this
a.BARK()