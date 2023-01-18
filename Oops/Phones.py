from Items import Item
class Phone(Item):

    
      def __init__(self,name,price,quantity,broken_phones=0):

        
        super().__init__(
        name,price,quantity )

        self.broken_phones = broken_phones
        # adding items in a list 
      

      def cigu(self):
        return "Gold flake tandimna bro"


