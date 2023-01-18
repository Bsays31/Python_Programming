class Clothing:
    Clothing_list = []

    def __init__(self,Product,Company,Design,Color,Price):
        self.Product = Product
        self.Company = Company
        self.Design = Design
        self.Price = Price
        self.Color = Color

        Clothing.Clothing_list.append(self)

    def __repr__(self):
        return f"{self.Product} : {self.Design} , {self.Price} , {self.Company} , {self.Color}"

    @classmethod
    def Clothing_stock(cls):
        for count,x in enumerate(Clothing.Clothing_list):
            print(count+1,".","Product :",x.Product," Company :",x.Company," Design :",x.Design," Color :",x.Color," Price :",x.Price)


    @classmethod
    def Purchase_clothing(cls):
        purchased = input("Enter the product :")

        for product1 in Clothing.Clothing_list:
            if purchased == product1.Product:
                return (product1.Price)

    @classmethod
    def Check_Company(cls):
        purchased = input("Enter the Brand of your product :")

        for product1 in Clothing.Clothing_list:
            if purchased == product1.Company:
                print(product1)

    @classmethod
    def Check_color(cls):
        purchased = input("Enter the color of your product :")

        for product1 in Clothing.Clothing_list:
            if purchased == product1.Color:
                return (product1)

    @classmethod
    def Check_design(cls):
        purchased = input("Enter the Design of the product :")

        for product1 in Clothing.Clothing_list:
            if purchased == product1.Design:
                return(product1)


tshirt1 = Clothing("T-shirt","Jockey","Round-neck","Black",600)
tshirt2 = Clothing("T-shirt","Jockey","Round-neck","Blue",600)
tshirt3 = Clothing("T-shirt","H&M","Round-neck","Purple",1200)
tshirt4 = Clothing("T-shirt","H&M","Round-neck","Orange",1200)
tshirt5 = Clothing("T-shirt","Roadster","Turtle-neck","White",1800)
tshirt6 = Clothing("T-shirt","HRX","V-neck","Red",1300)
denim1 = Clothing("Denim","Levis","Regular-fit","Grey",3200)
denim2 = Clothing("Denim","LEE","Carrot-fit","Navy-blue",2400)
denim3= Clothing("Denim","Buffalo","Skinny-fit","Grey",1200)
denim4 = Clothing("Denim","Reliance","Regular-fit","Grey",3200)
denim5 = Clothing("Denim","Levis","Regular-fit","Grey",4200)
jacket = Clothing("Jacket","Columbia","Wind-shield","Orange",6800)

