class Foo:
    def show(self):
        print("Hi")


def add_attribute(self):
    self.z = 9

Test = type('Test',(Foo,),{"x":77,"add_attribute" : add_attribute})
t = Test()
t.wy = "hello"
print(t.wy)
t.show()
t.add_attribute()
print(t.z)