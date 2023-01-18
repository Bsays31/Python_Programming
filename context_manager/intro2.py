# Making a context manager using class..
class File:
    def __init__(self,filename,method):
        self.file = open(filename,method)


# Whenever we use a context_manager we dont always have to use it as a context manager all the time, you can use it as other method 
# and in class without calling our other function that is required for the context manager to call like __enter__ and __exit__

    def __enter__(self):

        # This function is the first that happens and this function should returns something that we are going to use in the 
        # context_manager like "with something as "f" " , this something will call __enter__ and whatever __enter__ method we store
        # in "f" 
        
        print("Open")
        return self.file

        # Notice these are dundur methods cause it is going to be called in special way automatically from python because we are
        # can handle it in our own in here

    def __exit__(self,type,value,traceback):
        # What this does is regardless any exception in between enter and exit, this exit method will be called with that exception
        # and we can handle it in our own in here whatever the exception occurs it is sent to the exit

        print(f"{type} , {value} , {traceback}")
        # "type" = we use this "type" parameter to find out what the error actually is for example there is a Exception error
        # it will be handled in the code below but if there is any other error other than exception the program will crash....

        # "Value" = What is simply does is, it shows what type of value you enter in your file...

        # "traceback" = It show the address of the error..
        print("Exit")
        self.file.close()
        if type == Exception:
            return True
        # Note that, in this return statement we are telling python that we can handle this exception on our own and there is no 
        # need to crash the program...and also if there is anyother iregular error other than "Exception" the program will still crash


        # If exception are handled then we return True but be careful with it cause if there are some exception to be handled 
        # then handle is first then only return true 


# The reason why i am able to do this is because we have a enter and exit method defining that this is a context_manger

with File("File1.txt","w") as file:
    print("Middle")
    file.write("Hello this is Bishesh gurung")
    raise Exception
    # Note that, the program wont run if there is a syntax error or an intentional effort to make an error other raising exception
    #raise FileExistsError()
    # Now this error will crash the program as this is not an exception...but will still close the file that was opened...