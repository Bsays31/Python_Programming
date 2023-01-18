import csv
class Item :

    pay_rate = 0.8
    all_items = []
    
    def __init__(self,name,price,quantity):

        #assigning items with their attributes 
        self.__names = name
        self.__price = price
        self.quantity = quantity

        # adding items in a list 
        Item.all_items.append(self)


    @property
    def name(self):
        print("getter")
        return self.__names

    @name.setter
    def changename(self,name):
        print("setter")
        self.__names = name

    def apply_increment(self,increment):
        self.__price = self.__price + self.__price * increment


    def printprice(self):
        return self.__price

    def calculate(self):
        return self.__price * self.quantity

    def print_item(self):
        print(self.name)
        print(self.__price)
        print(self.quantity)   
    
    @classmethod
    def instanciate_obj_csv(cls):
            with open('products.csv','r') as f:
                csv_reader = csv.DictReader(f)
                items = list(csv_reader)

                for x in items:
                    Item(
                        name =  x.get('name'),
                        price = x.get('price'),
                        quantity= x.get('quantity')

                    )
                    return x

    def cigu(self):
        return "Flake tandimna hau som"

    def distcount(self):
         self.__price = self.__price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__} ( '{self.name}' , {self.__price} , {self.quantity} )"

    def __connet(self,stp_server):
            pass


    def __body(self):
        return f"""
            this is price {self.__price}
        
        """
    def __send(self):
        pass
   
    def send_email(self):
        self.__connet("Ssss")
        self.__body()
        self.__send()

# Bishesh = Item("Oppo",23000,2)
# print(Item.name)

print(Item.instanciate_obj_csv())


