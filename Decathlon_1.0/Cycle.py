class Cycle:

    stock_list = []



    def __init__(self,Product,Company,Model,Price,Color):
        self.Product = Product
        self.Company = Company
        self.Model = Model
        self.Price = Price
        self.Color = Color

        Cycle.stock_list.append(self)

    @classmethod
    def Cycle_instock(cls):
        for count,x in enumerate(Cycle.stock_list):
            print("\n",count+1,". Product :" ,x.Product ,"  Brand :", x.Company ,"  Model :", x. Model ,"  Price :", x.Price,"  Color :",x.Color)

    @classmethod
    def Buy_product(cls):
        product1 = input("Enter the company :")

        for product in Cycle.stock_list:
            if product1 in product.Company:
                return(product.Price)

    @classmethod
    def Product_model(cls):
        product1 = input("Enter the Model :")

        for product in Cycle.stock_list:
            if product1 in product.Model:
                return(product)

    @classmethod
    def Product_color(cls):
        product1 = input("Enter the Color :")

        for product in Cycle.stock_list:
            if product1 in product.Color:
                return(product)



    def __repr__(self):
        return f"{self.__class__.__name__} :  {self.Company} , {self.Model} , {self.Color} , {self.Price}"

    
bishesh1 = Cycle("Cycle","Hero","Road-bike",20000,"Glossy-red")
bishesh2 = Cycle("Cycle","Indian","Road-bike",14000,"Green")
bishesh3 = Cycle("Cycle","Trek","MTB",120000,"Matte-Silver")
bishesh4 = Cycle("Cycle","Ninety-One","Electric-bike",80000,"Matte-brown")
bishesh5 = Cycle("Cycle","Rodeo","Fat-bike",21000,"White")
bishesh6 = Cycle("Cycle","Kripsta","Road-bike",18000,"Yellow")
bishesh7 = Cycle("Cycle","Avon","Hardtail",230000,"Black")

# Cycle.Product_model()