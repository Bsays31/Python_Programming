def args(*args):
    for arg in args:
        print(arg)

def kwargs(**kwargs):
    for key,value in kwargs.keys():
        print(key,value)




args("Hello","this","is","Bishesh","Gurung")
kwargs(Name="Bishesh",Age="22",Sex="Male")