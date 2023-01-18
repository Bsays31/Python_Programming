#Creating a class
class Guitar:

    def __init__(self):
        self.strings = 6
        #Private member 
        self.__cost = 50
        self.play()

    def play(self):
        print("Ta d ta da ta da")

    # def __print_private(self):
    #     print("The cost of the product is",self.)


# bishesh = Guitar()
# print(bishesh._Guitar__cost)