from main import Vehicle
import csv

class Bike(Vehicle):

    bike_stock = []

    def __init__(self,Company:str,Model,Price:int,Cubic_centimeter:int,Road_legal:int):
        self.Company = Company
        self.Model = Model
        self.Price = Price
        self.Cubic_centimeter = Cubic_centimeter
        self.Road_legal = Road_legal

        Bike.bike_stock.append(self)


    def __repr__(self):
        return f"({self.Company} : {self.Model} , {self.Price} , {self.Cubic_centimeter} , {self.Road_legal})"


    @classmethod
    def types_of_vehicle(cls):
        for count,x in enumerate(Bike.bike_stock):
            print(count+1,".","Company :",x.Company," Model :",x.Model," Price :",x.Price," Cubic centimeter :",x.Cubic_centimeter," Road legal :",x.Road_legal)

    def vehicle_lifespan(self):
        return super().vehicle_lifespan()

    @classmethod
    def new_bikes(cls):
        with open("Bike_stock.csv","a") as bike:
            csv_writer = csv.writer(bike)

            a = int(input("How many bikes have arrived :"))
            while a != 0 :
                Company = input("Enter the Company of the vehicle :")
                Model = input("Enter the model of the vehicle :")
                Price = int(input("ENter the price of the vehicle :"))
                Cubic_centimeter = int(input("Enter how many cc :"))
                Road_legal = int(input("Enter the legal duration of the bike :"))
                a1 = [Company,Model,Price,Cubic_centimeter,Road_legal]
                #Fields = [Company,Model,Price,Cubic_centimeter,Road_legal]
                
                csv_writer.writerow(a1)
                a-=1

    def Purchase(self):
        return super().Purchase()


Bike.new_bikes()