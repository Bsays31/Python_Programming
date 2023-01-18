class Sports_equipment:

    equipment = []


    def __init__(self,Product,Company,Model,Material,Price):
        self.Product = Product
        self.Company = Company
        self.Model = Model
        self.Material = Material
        self.Price = Price

        Sports_equipment.equipment.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.Product} , {self.Company} , {self.Model} , {self.Material} , {self.Price}"

    @classmethod
    def Equipment_stock(cls):
        for count,x in enumerate(Sports_equipment.equipment):
            print(count+1,". Product:",x.Product," Company :",x.Company," Model:",x.Model," Material:",x.Material," Price:",x.Price,"\n")

    @classmethod
    def Purchase_eq(cls):
        a = input("Enter the Equipment :")
        
        for product in Sports_equipment.equipment:
            if a in product.Product:
                return(product.Price)

    @classmethod
    def Check_company(cls):
        a = input("Enter the company of the equipment you're looking for :")
        
        for product in Sports_equipment.equipment:
            if a in product.Company:
                return(product)

    @classmethod
    def Check_material(cls):
        a = input("Enter the material of the equipment you're looking for :")
        
        for product in Sports_equipment.equipment:
            if a in product.Material:
                return(product)


gym = Sports_equipment("Gym","VIVA","Leg-press","Metal",80000)
gym = Sports_equipment("Gym","Olympic","Squad-rack","Metal",230000)
gym = Sports_equipment("Gym","Olympic","Chest-press","Metal",870000)
trekking = Sports_equipment("Trekking","Columbia","Trekking-bag","Ployster",5400)
running = Sports_equipment("Running","Decathlon","Hydration-bag","Polyster",3200)
boxing = Sports_equipment("Boxing","Jab-cross","Gloves","Leather",2500)

