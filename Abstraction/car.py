from main import Vehicle
import csv
class Car(Vehicle):

    car_stock = []

    def __init__(self,Company,Model,Price,Color,Life_span,Cubic_centimeter):
        self.Company = Company
        self.Model = Model
        self.Price = Price
        self.Color = Color
        self.Life_span = Life_span
        self.Cubic_centimeter = Cubic_centimeter
        
           
        Car.car_stock.append(self)
    

    @classmethod
    def types_of_vehicle(cls):
       for count,x in enumerate(Car.car_stock):
         print(count+1,".","Company :",x.Company," Model :",x.Model," Price :",x.Price," Color :",x.Color," Life_span :",x.Life_span," Cubic centimeter :",x.Cubic_centimeter)

    @classmethod
    def New_stock(cls):
        with open("Car_stock.csv","a") as a :
            csv_writer = csv.writer(a)

            i = int(input("How many cars have arrived :"))
            while i != 0 :
                Company = input("Enter the name of the company :") 
                Model = input("Enter the model of the company :")
                Price = int(input("Enter the price of the company :"))
                Color = input("Enter the color of the vehicle :")
                Life_span = int(input("Enter the life span of the vehicle :"))
                
                b = [Company,Model,float(Price),Color,Life_span]

               
                csv_writer.writerow(b) 
                print("Updated!!")
                i-=1


    def __repr__(self):
        return f"({self.Company} , {self.Model} , {self.Price} , {self.Color} , {self.Life_span} , {self.Cubic_centimeter})"

    @classmethod
    def intantiating_object(cls):
        with open("Car_stock.csv","r") as b:
            csv_reader = csv.DictReader(b)
            data = list(csv_reader)
        
            for x in data:
                Car(
                    Company = x.get('Company'),
                    Model = x.get('Model'),
                    Price = x.get('Price'),
                    Color = x.get('Color'),
                    Life_span = x.get('Life_span'),
                    Cubic_centimeter = x.get('Cubic_centimeter')
                )

    @classmethod
    def Purchase(cls):
        for count,x in enumerate(Car.car_stock):
            print(count+1,".","Company :",x.Company," Model :",x.Model," Price :",x.Price," Color :",x.Color," Life_span :",x.Life_span," Cubic centimeter :",x.Cubic_centimeter)
        
        product = input("Enter the company of the vehicle you want to buy :")

        for x in Car.car_stock:
            if product in x.Company:
                print("The Price of this vehicle is :",x.Price)
                
        
    @classmethod
    def vehicle_lifespan(cls):
        veh = input("Enter the product you want to know the life span of :")

        for product in Car.car_stock:
            if veh == product.Company:
                print("The Life span of this Vehicle is :",product.Life_span,"years")


# Car.New_stock()
Car.intantiating_object()
# print(Car.car_stock)

# #Car.types_of_vehicle()
# Car.vehicle_lifespan()
Car.Purchase()


car2 = Car("Honda","Sports",5000000,"Red",15,250)