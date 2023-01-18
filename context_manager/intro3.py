# Import contextlib
from contextlib import contextmanager

# In this context lib there is a decorator that allows us to decorate a generator 

@contextmanager
def file(filename,method):
    # You can think this as __enter__
    print("Enter")
    file = open(filename,method)
    yield file

    # And this as a exit
    file.close()
    print("Exit")

    return True
    # With this you can handle all the exception and other errors


with file("Text.txt","w") as f:
    print("Middle")
    f.write("Hello there!")xx