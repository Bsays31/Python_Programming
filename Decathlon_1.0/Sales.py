from Store import Decathlon
from Cycle import Cycle
from Sports_eq import Sports_equipment
from Clothing import Clothing
# Sports-equipment : Equipment_stock():cls , Purchase_eq():cls, Check_company(cls) , Check_material(cls)

# Cycle: Cycle_instock(cls) , Buy_product(cls) , Product_model(cls) , Product_color(cls)

# Clothing : Clothing_stock():cls , Purchase_clothing():cls , Check_company(cls) , Check_color(cls), Check_design(cls)

class Sales(Decathlon,Cycle,Sports_equipment,Clothing):


    all_stock = Cycle.stock_list + Sports_equipment.equipment + Clothing.Clothing_list


    def __init__(self, Product):
        super().__init__(Product)


    def __repr__(self):
        return f"{self.__class__.__name__} : We thank you for your support..."

 
    @classmethod
    def Display_allstock(cls):
        for count,x in enumerate(Sales.all_stock):
            print(count+1,".",x)


    @classmethod
    def Buy_product(cls):
        print("Welcome to Decathlon !!",)
        Select = input("What product would you like to buy please enter : ")
        
        for product in Sales.all_stock:
            if Select == product.Product:
                print(product.Company,end=", ");
                
            b = product
        Company = input("\nCompany name : ")
        for c in Sales.all_stock:
            if Company == c.Company:
                print(c)
                return c.Price


Sales.Display_allstock()
Sales.Buy_product()
  



