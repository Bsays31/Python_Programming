# Calculate Depreciation of value ?

# As the value depreciating per year is 20%

price = int(input("Enter the price of the product to know how much is it worth after use :"))


time = int(input("Enter the time period in days :"))

if time > 365:
    depreciation = (price * 20 // 100)-price
    print("The depreciated value of the product is",depreciation)
else:
    print("This product is under warrenty")    
