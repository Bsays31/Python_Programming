from Parent import Guitar
class Electric(Guitar):

    def __init__(self):

        #Using the super method to inherit the Guitar class
        super().__init__()
        
        #Modifying the perimeter 
        self.strings = 8
        self.music()

    def music(self):
        print("Until i found her!")

    def __secret(self):
        pass

brian = Electric()
print(brian.strings)