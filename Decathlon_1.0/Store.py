import csv
class Decathlon:

    items = []
    debit_card_purchase = 1000
    Roi = 8
    period = 12
      


    def __init__(self,Product):
        self.Product = Product
        

        Decathlon.items.append(self)

    @classmethod
    def Instantiating_object(cls):
        with open ("Product.csv","r") as a:
            csv_reader = csv.DictReader(a)
            instantiating = list(csv_reader)

            for x in instantiating:
                Decathlon(
                    Product = x.get("Product")
                )

            
    def __repr__(self):
        return f"{self.__class__.__name__}  {self.Product}"


    @classmethod
    def Debit_purchase(cls,ab):
        return ab - Decathlon.debit_card_purchase

    @classmethod
    def emi(cls,a):
      decimal = Decathlon.Roi / 100
      interest_per_month = decimal / 12
      dec2 = interest_per_month + 1
      i = Decathlon.period
      grand_total = 0
      while i != 0:
        divide = 1 / dec2
        grand_total =  grand_total + divide
        i -= 1

      b = 1 / grand_total
      multiply = b * a
      return "The EMI of this product will be",multiply,"per month."
      


Decathlon.Instantiating_object()